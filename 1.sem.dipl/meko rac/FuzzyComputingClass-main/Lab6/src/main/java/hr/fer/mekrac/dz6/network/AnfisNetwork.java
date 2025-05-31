package hr.fer.mekrac.dz6.network;

import hr.fer.mekrac.dz6.Sample;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

/**
 * @author matejc
 * Created on 28.12.2022.
 */

public class AnfisNetwork {
    private final Random random = new Random();
    private final int ruleNum;
    private final int batchSize;

    private final Parameters parameters;


    public AnfisNetwork(int ruleNum, int batchSize) {
        this.ruleNum = ruleNum;
        this.batchSize = batchSize;

        parameters = new Parameters(ruleNum, random);
    }

    public Parameters getParameters() {
        return parameters;
    }


    public List<Double> train(List<Sample> samples, int iterationsNumber, double learningRate) {
        List<Double> errors = new ArrayList<>(iterationsNumber / 100);
        for (int iteration = 0; iteration < iterationsNumber; iteration++) {
            Collections.shuffle(samples, random);

            double error = samples.stream()
                    .mapToDouble(sample -> Math.pow(sample.z() - predict(sample.x(), sample.y()), 2) / 2)
                    .average().orElseThrow();

            errors.add(error);

            if (iteration % 100 == 0) {
                System.out.printf("Iteration %d, error: %.4f%n", iteration, error);
            }

            int batchBeginning = 0;
            int batchEnd = batchSize - 1;

            while (batchEnd < samples.size()) {
                var batch = samples.subList(batchBeginning, batchEnd);

                DerivationVariables dVars = new DerivationVariables(ruleNum);

                for (Sample sample : batch) {
                    double x = sample.x();
                    double y = sample.y();
                    double expected = sample.z();

                    double numerator = 0;
                    double piSum = 0;

                    for (int i = 0; i < ruleNum; i++) {
                        dVars.alpha[i] = 1.0 / (1 + Math.exp(parameters.b[i] * (x - parameters.a[i])));
                        dVars.beta[i] = 1.0 / (1 + Math.exp(parameters.d[i] * (y - parameters.c[i])));
                        dVars.pi[i] = dVars.alpha[i] * dVars.beta[i];
                        dVars.z[i] = (parameters.p[i] * x + parameters.q[i] * y + parameters.r[i]);

                        piSum += dVars.pi[i];
                        numerator += dVars.pi[i] * dVars.z[i];
                    }

                    if (piSum == 0) piSum = Double.NaN;
                    double output = numerator / piSum;

                    double dEdO = -(expected - output);

                    for (int i = 0; i < ruleNum; i++) {
                        double dEdZ = dEdO * dVars.pi[i] / piSum;

                        dVars.dP[i] += dEdZ * x;
                        dVars.dQ[i] += dEdZ * y;
                        dVars.dR[i] += dEdZ;

                        double dOdPiNumerator = 0;
                        for (int j = 0; j < ruleNum; j++) {
                            if (i != j)
                                dOdPiNumerator += (dVars.z[i] - dVars.z[j]) * dVars.pi[j];
                        }
                        double dOdPi = dOdPiNumerator / (piSum * piSum);

                        dVars.dA[i] += dEdO * dOdPi * dVars.beta[i] * parameters.b[i] * dVars.alpha[i] * (1 - dVars.alpha[i]);
                        dVars.dB[i] += dEdO * dOdPi * dVars.beta[i] * -(x - parameters.a[i]) * dVars.alpha[i] * (1 - dVars.alpha[i]);
                        dVars.dC[i] += dEdO * dOdPi * dVars.alpha[i] * parameters.d[i] * dVars.beta[i] * (1 - dVars.beta[i]);
                        dVars.dD[i] += dEdO * dOdPi * dVars.alpha[i] * -(y - parameters.c[i]) * dVars.beta[i] * (1 - dVars.beta[i]);
                    }

                }

                updateParams(dVars, learningRate);

                batchEnd += batchSize;
            }

        }
        return errors;
    }

    private void updateParams(DerivationVariables dVars, double learningRate) {
        for (int i = 0; i < ruleNum; i++) {
            parameters.a[i] -= learningRate * dVars.dA[i];
            parameters.b[i] -= learningRate * dVars.dB[i];
            parameters.c[i] -= learningRate * dVars.dC[i];
            parameters.d[i] -= learningRate * dVars.dD[i];
            parameters.p[i] -= learningRate * dVars.dP[i];
            parameters.q[i] -= learningRate * dVars.dQ[i];
            parameters.r[i] -= learningRate * dVars.dR[i];
        }
    }

    public double predict(double x, double y) {
        double numerator = 0;
        double denominator = 0;

        for (int i = 0; i < ruleNum; i++) {
            double alpha = 1.0 / (1 + Math.exp(parameters.b[i] * (x - parameters.a[i])));
            double beta = 1.0 / (1 + Math.exp(parameters.d[i] * (y - parameters.c[i])));
            double pi = alpha * beta;
            double z = (parameters.p[i] * x + parameters.q[i] * y + parameters.r[i]);

            denominator += pi;
            numerator += pi * z;
        }

        if (denominator == 0) return Double.NaN;
        return numerator / denominator;
    }
}
