package hr.fer.mekrac.lab7.selection;

import hr.fer.mekrac.lab7.network.NeuralNetwork;

import java.util.List;

/**
 * @author matejc
 * Created on 14.01.2023.
 */

@FunctionalInterface
public interface ISelectionAlgorithm {
    List<NeuralNetwork> selectFromPopulation(List<NeuralNetwork> population, double[] errors, int n);
}
