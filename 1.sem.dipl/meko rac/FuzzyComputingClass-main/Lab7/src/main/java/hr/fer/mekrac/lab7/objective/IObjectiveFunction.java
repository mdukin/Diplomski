package hr.fer.mekrac.lab7.objective;

import hr.fer.mekrac.lab7.network.NeuralNetwork;

/**
 * @author matejc
 * Created on 13.01.2023.
 */

@FunctionalInterface
public interface IObjectiveFunction {
    double valueAt(NeuralNetwork network);
}
