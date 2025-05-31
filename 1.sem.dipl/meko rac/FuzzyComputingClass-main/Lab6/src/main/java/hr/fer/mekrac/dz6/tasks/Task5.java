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

public class Task5 {
    private static final int BATCH_SIZE = 9;
    private static final double LEARNING_RATE = 1E-4;
    private static final int RULES = 6;

    public static void main(String[] args) {
        var samples = SampleFactory.sampleFunction(SampleFactory.LAB_FUNCTION, -4, 4, -4, 4);

        AnfisNetwork anfisNetwork = new AnfisNetwork(RULES, BATCH_SIZE);
        anfisNetwork.train(samples, 20_000, LEARNING_RATE);

        List<double[]> results = new ArrayList<>();
        for (double x = -4; x < 4; x += 0.1) {
            double[] values = new double[13];
            values[0] = x;
            for (int rule = 0; rule < RULES; rule++) {
                double a = anfisNetwork.getParameters().getA()[rule];
                double b = anfisNetwork.getParameters().getB()[rule];
                double c = anfisNetwork.getParameters().getC()[rule];
                double d = anfisNetwork.getParameters().getD()[rule];

                values[1 + 2 * rule] = sigmoid(a, b, x);
                values[1 + 2 * rule + 1] = sigmoid(c, d, x);
            }
            results.add(values);
        }

        OutputWriter.writeArraysToFile("task5.txt", results);
    }

    private static double sigmoid(double a, double b, double x) {
        return 1.0 / (1 + Math.exp(b * (x - a)));
    }
}
