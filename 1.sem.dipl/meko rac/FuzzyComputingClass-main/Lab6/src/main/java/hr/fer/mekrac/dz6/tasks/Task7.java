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

public class Task7 {
    private static final double LEARNING_RATE = 5E-4;
    private static final int RULES = 6;

    public static void main(String[] args) {
        var samples = SampleFactory.sampleFunction(SampleFactory.LAB_FUNCTION, -4, 4, -4, 4);

        List<Integer> batchSizes = List.of(1, 9, 81);

        for (var batch : batchSizes) {
            AnfisNetwork anfisNetwork = new AnfisNetwork(RULES, batch);
            var errors = anfisNetwork.train(samples, 20_000, LEARNING_RATE);

            List<double[]> output = new ArrayList<>();

            for (int i = 0; i < errors.size(); i++) {
                double error = errors.get(i);
                double[] value = new double[]{i, error};
                output.add(value);
            }

            OutputWriter.writeArraysToFile("task7-%d.txt".formatted(batch), output);

        }

    }
}
