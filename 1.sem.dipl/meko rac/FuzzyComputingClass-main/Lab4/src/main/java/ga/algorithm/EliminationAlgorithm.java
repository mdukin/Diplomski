package ga.algorithm;

import ga.data.Solution;
import ga.function.MeanSquareLossFunction;

import java.util.Comparator;
import java.util.List;

/**
 * @author matejc
 * Created on 14.11.2022.
 */

public class EliminationAlgorithm extends GeneticAlgorithm {

    public EliminationAlgorithm(MeanSquareLossFunction lossFunction,
                                int variables, int populationSize,
                                int minValue, int maxValue,
                                int generations,
                                double mutationChance) {
        super(lossFunction, variables, populationSize, minValue, maxValue, mutationChance, generations);
    }

    @Override
    public Solution run() {
        List<Solution> population = createInitialPopulation();

        for (int i = 0; i < generations; i++) {
            List<Solution> selection = selectByRouletteWheel(population, 3);

            Solution worst = findWorstSolution(selection);
            selection.remove(worst);
            population.remove(worst);

            Solution child = cross(selection.get(0), selection.get(1));
            child = mutate(child);

            population.add(child);

            Solution bestSolution = bestSolution(population);

            System.out.printf("Iteration %d, best: %s, f: %f%n", i + 1, bestSolution, lossFunction.valueAt(bestSolution));
        }

        return bestSolution(population);
    }

    private Solution findWorstSolution(List<Solution> selection) {
        return selection.stream()
                .max(Comparator.comparing(lossFunction::valueAt))
                .orElseThrow();
    }
}
