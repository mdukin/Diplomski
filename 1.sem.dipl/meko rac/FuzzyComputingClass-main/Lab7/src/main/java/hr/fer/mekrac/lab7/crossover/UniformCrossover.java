package hr.fer.mekrac.lab7.crossover;

import static hr.fer.mekrac.lab7.util.Common.RANDOM;

/**
 * @author matejc
 * Created on 13.01.2023.
 */

public class UniformCrossover implements ICrossover {
    @Override
    public double[] crossover(double[] parent1, double[] parent2) {
        if (parent1.length != parent2.length) throw new IllegalArgumentException("Parent sizes differ.");

        double[] child = new double[parent1.length];

        for (int i = 0; i < child.length; i++) {
            child[i] = RANDOM.nextBoolean() ? parent1[i] : parent2[i];
        }

        return child;
    }
}
