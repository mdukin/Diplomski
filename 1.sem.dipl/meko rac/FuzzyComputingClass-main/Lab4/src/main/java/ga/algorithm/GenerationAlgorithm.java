package ga.algorithm;

import ga.data.Solution;
import ga.function.MeanSquareLossFunction;

import java.util.ArrayList;
import java.util.List;

/**
 * @author matejc
 * Created on 14.11.2022.
 */

public class GenerationAlgorithm extends GeneticAlgorithm {

    private final boolean elitism;

    public GenerationAlgorithm(MeanSquareLossFunction lossFunction,
                               int variables, int populationSize,
                               int minValue, int maxValue,
                               double mutationChance, int generations,
                               boolean elitism) {
        super(lossFunction, variables, populationSize, minValue, maxValue, mutationChance, generations);

        this.elitism = elitism;
    }

    @Override
    public Solution run() {
        List<Solution> population = createInitialPopulation();

        for (int i = 0; i < generations; i++) {
            List<Solution> newPopulation = new ArrayList<>(populationSize);

            if (elitism) newPopulation.add(bestSolution(population));

            while (newPopulation.size() != populationSize) {
                List<Solution> selection = selectByRouletteWheel(population, 2);
                Solution child = cross(selection.get(0), selection.get(1));
                child = mutate(child);

                newPopulation.add(child);
            }
            population = newPopulation;
            lossFunction.initCache();

            Solution bestSolution = bestSolution(population);
            System.out.printf("Iteration %d, best: %s, f: %f%n", i + 1, bestSolution, lossFunction.valueAt(bestSolution));
        }

        return bestSolution(population);
    }
}
