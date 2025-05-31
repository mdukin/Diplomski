package hr.fer.mekrac.lab7.crossover;

import hr.fer.mekrac.lab7.util.Common;
import lombok.RequiredArgsConstructor;

/**
 * @author matejc
 * Created on 13.01.2023.
 */

@RequiredArgsConstructor
public class ArithmeticCrossover implements ICrossover {

    @Override
    public double[] crossover(double[] parent1, double[] parent2) {
        if (parent1.length != parent2.length) throw new IllegalArgumentException("Parent sizes differ.");

        double lambda = Common.RANDOM.nextDouble();

        double[] child = new double[parent1.length];

        for (int i = 0; i < child.length; i++) {
            child[i] = parent1[i] * lambda + (1 - lambda) * parent2[i];
        }

        return child;
    }
}
