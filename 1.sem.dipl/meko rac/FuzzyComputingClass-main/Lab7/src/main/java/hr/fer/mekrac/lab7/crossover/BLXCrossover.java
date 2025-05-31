package hr.fer.mekrac.lab7.crossover;

import hr.fer.mekrac.lab7.util.Common;
import lombok.RequiredArgsConstructor;

/**
 * @author matejc
 * Created on 13.01.2023.
 */

@RequiredArgsConstructor
public class BLXCrossover implements ICrossover {

    private final double alpha;

    @Override
    public double[] crossover(double[] parent1, double[] parent2) {
        if ((parent1.length != parent2.length)) throw new IllegalArgumentException("Parents differ in size.");

        double[] child = new double[parent1.length];

        for (int i = 0; i < parent1.length; i++) {
            double min = Math.min(parent1[i], parent2[i]);
            double max = Math.max(parent1[i], parent2[i]);

            double diff = max - min;

            if (diff==0) diff = 1E-5;

            child[i] = Common.RANDOM.nextDouble(min - diff * alpha, max + diff * alpha);
        }
        return child;
    }
}
