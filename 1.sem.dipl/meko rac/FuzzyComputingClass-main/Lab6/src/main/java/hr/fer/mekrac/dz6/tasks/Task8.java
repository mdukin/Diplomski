package hr.fer.mekrac.dz6.tasks;

import hr.fer.mekrac.dz6.SampleFactory;
import hr.fer.mekrac.dz6.network.AnfisNetwork;
import hr.fer.mekrac.dz6.output.OutputWriter;

import java.util.ArrayList;
import java.util.List;

/**
 * @author matejc
 * Created on 28.12.2022.
 */

public class Task8 {
    private static final int RULES = 6;

    public static void main(String[] args) {
        var samples = SampleFactory.sampleFunction(SampleFactory.LAB_FUNCTION, -4, 4, -4, 4);

        List<Integer> batchSizes = List.of(1, 81);
        List<Double> learningRates = List.of(1E-2, 1E-3, 1E-4, 1E-6, 0.5);

        for (var batch : batchSizes) {
            for (var learningRate : learningRates) {
                AnfisNetwork anfisNetwork = new AnfisNetwork(RULES, batch);
                var errors = anfisNetwork.train(samples, 1_000, learningRate);

                List<double[]> output = new ArrayList<>();

                for (int i = 0; i < errors.size(); i++) {
                    double error = errors.get(i);
                    double[] value = new double[]{i, error};
                    output.add(value);
                }

                OutputWriter.writeArraysToFile("task8-%d-%f.txt".formatted(batch, learningRate), output);
            }

        }
    }
}
