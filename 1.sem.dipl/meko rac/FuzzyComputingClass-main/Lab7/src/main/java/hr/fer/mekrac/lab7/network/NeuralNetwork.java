package hr.fer.mekrac.lab7.network;

import hr.fer.mekrac.lab7.util.Common;
import lombok.Getter;

import java.util.Arrays;

/**
 * @author matejc
 * Created on 13.01.2023.
 */

@Getter
public class NeuralNetwork {
    private final int[] structure;
    private final double[] outputs;
    private final double[] parameters;


    public NeuralNetwork(double initStddev, int... structure) {
        this.structure = structure;
        this.outputs = new double[numberOfNeurons(structure)];
        this.parameters = new double[numberOfParameters(structure)];

        initializeParameters(initStddev);
    }

    public NeuralNetwork(double[] parameters, int... structure) {
        this.structure = structure;
        this.parameters = parameters;
        this.outputs = new double[numberOfNeurons(structure)];
    }

    private void initializeParameters(double initStddev) {
        for (int i = 0; i < parameters.length; i++) {
            parameters[i] = Common.RANDOM.nextGaussian(0, initStddev);
        }
    }

    public double[] calcOutput(double[] input) {
        // First layer (no parameters)
        System.arraycopy(input, 0, outputs, 0, structure[0]);

        int outputIndex = structure[0];
        int paramIndex = 0;

        // Second layer
        for (int i = 0; i < structure[1]; i++) {
            double sum = 0;
            for (int j = 0; j < structure[0]; j++) {
                double w = parameters[paramIndex];
                double s = parameters[paramIndex + 1];
                sum += Math.abs(input[j] - w) / Math.abs(s);

                paramIndex += 2;
            }
            outputs[outputIndex + i] = 1.0 / (1.0 + sum);
        }
        outputIndex += structure[1];

        // Remaining layers
        for (int layer = 2; layer < structure.length; layer++) {
            for (int i = 0; i < structure[layer]; i++) {
                double sum = 0;
                for (int j = 0; j < structure[layer - 1]; j++) {
                    sum += outputs[outputIndex - structure[layer - 1] + j] * parameters[outputIndex + i * structure[layer - 1] + j];
                }
                sum += parameters[outputIndex + i * structure[layer - 1] + structure[layer - 1]]; // bias
                outputs[outputIndex + i] = sigmoid(sum);
            }
            outputIndex += structure[layer];
        }

        int numResultOutputs = structure[structure.length - 1];
        double[] finalOutput = new double[numResultOutputs];

        System.arraycopy(outputs, outputs.length - numResultOutputs, finalOutput, 0, numResultOutputs);

        return finalOutput;
    }

    private static int numberOfNeurons(int... structure) {
        return Arrays.stream(structure)
                .sum();
    }

    private static int numberOfParameters(int... structure) {
        int inputLayer = structure[0];
        int lastLayer = structure[1];

        int params = inputLayer * lastLayer * 2;

        for (int i = 2; i < structure.length; i++) {
            params += structure[i] * (structure[i - 1] + 1);
        }
        return params;
    }

    private double sigmoid(double x) {
        return 1 / (1 + Math.exp(-x));
    }
}
