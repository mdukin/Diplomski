package hr.fer.mekrac.lab7.evolution;

import hr.fer.mekrac.lab7.crossover.ICrossover;
import hr.fer.mekrac.lab7.mutation.IMutation;
import hr.fer.mekrac.lab7.network.NeuralNetwork;
import hr.fer.mekrac.lab7.objective.IObjectiveFunction;
import hr.fer.mekrac.lab7.selection.ISelectionAlgorithm;
import lombok.RequiredArgsConstructor;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * @author matejc
 * Created on 13.01.2023.
 */

@RequiredArgsConstructor
public class GenerationEvolutionAlgorithm implements IAlgorithm {

    private final int[] structure;
    private final int populationSize;
    private final int generations;
    private final double zeroError;
    private final double initStddev;
    private final IMutation mutation;
    private final ICrossover crossover;
    private final IObjectiveFunction objectiveFunction;
    private final ISelectionAlgorithm selectionAlgorithm;

    public NeuralNetwork run() {
        List<NeuralNetwork> population = createInitialPopulation();

        NeuralNetwork bestSolution;

        System.out.printf("Running for %d generations.%n", generations);

        for (int i = 0; i < generations; i++) {
            List<NeuralNetwork> newPopulation = new ArrayList<>();

            double[] errors = calculateErrors(population);
            bestSolution = getBestFromErrors(population, errors);

            newPopulation.add(bestSolution);

            if (objectiveFunction.valueAt(bestSolution) <= zeroError) {
                System.out.println("Error reached zero. Exiting.");
                return bestSolution;
            }

            if (i % 1000 == 0)
                System.out.printf("Generation %d,\tbest: %f%n", i, objectiveFunction.valueAt(bestSolution));

            while (newPopulation.size() != populationSize) {
                var selection = selectionAlgorithm.selectFromPopulation(population, errors, 2);
                double[] childParameters = crossover.crossover(selection.get(0).getParameters(), selection.get(1).getParameters());
                NeuralNetwork child = new NeuralNetwork(childParameters, structure);
                mutation.mutate(child.getParameters());

                newPopulation.add(child);
            }
            population = newPopulation;

        }

        return bestSolution(population);
    }

    private NeuralNetwork getBestFromErrors(List<NeuralNetwork> population, double[] errors) {
        int minIndex = 0;
        double minError = Double.MAX_VALUE;

        for (int i = 0; i < errors.length; i++) {
            if (errors[i] < minError) {
                minIndex = i;
                minError = errors[i];
            }
        }
        return population.get(minIndex);
    }

    private double[] calculateErrors(List<NeuralNetwork> population) {
        double[] errors = new double[population.size()];
        for (int i = 0; i < population.size(); i++) {
            NeuralNetwork neuralNetwork = population.get(i);
            errors[i] = objectiveFunction.valueAt(neuralNetwork);
        }
        return errors;
    }

    private List<NeuralNetwork> createInitialPopulation() {
        List<NeuralNetwork> population = new ArrayList<>(populationSize);

        while (population.size() != populationSize) {
            population.add(new NeuralNetwork(initStddev, structure));
        }
        return population;
    }

    private NeuralNetwork bestSolution(List<NeuralNetwork> population) {
        return population.stream()
                .min(Comparator.comparing(objectiveFunction::valueAt))
                .orElseThrow();
    }

}
