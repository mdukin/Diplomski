package hr.fer.mekrac.lab7.crossover;

import java.util.Arrays;
import java.util.List;

import static hr.fer.mekrac.lab7.util.Common.RANDOM;

/**
 * @author matejc
 * Created on 13.01.2023.
 */

public class CombinedCrossover implements ICrossover {

    private final List<ICrossover> crossoverAlgorithms;

    public CombinedCrossover(ICrossover... crossoverAlgorithms) {
        this.crossoverAlgorithms = Arrays.asList(crossoverAlgorithms);
    }

    @Override
    public double[] crossover(double[] parent1, double[] parent2) {

        return crossoverAlgorithms.get(RANDOM.nextInt(crossoverAlgorithms.size()))
                .crossover(parent1, parent2);
    }
}
