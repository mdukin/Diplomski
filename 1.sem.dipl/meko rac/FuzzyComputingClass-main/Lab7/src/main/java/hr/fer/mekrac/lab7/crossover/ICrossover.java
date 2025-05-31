package hr.fer.mekrac.lab7.crossover;

/**
 * @author matejc
 * Created on 13.01.2023.
 */

@FunctionalInterface
public interface ICrossover {
    double[] crossover(double[] parent1, double[] parent2);
}
