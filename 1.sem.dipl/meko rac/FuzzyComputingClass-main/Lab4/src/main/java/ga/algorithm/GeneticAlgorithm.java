package ga.algorithm;

import ga.data.Solution;
import ga.function.MeanSquareLossFunction;
import ga.util.Common;
import org.apache.commons.math3.linear.ArrayRealVector;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

/**
 * @author matejc
 * Created on 14.11.2022.
 */

public abstract class GeneticAlgorithm implements IAlgorithm<Solution> {
    protected final MeanSquareLossFunction lossFunction;
    private final int variablesNumber;
    protected final int populationSize;
    protected final int minValue;
    protected final int maxValue;
    private final double mutationChance;
    protected final int generations;

    protected GeneticAlgorithm(MeanSquareLossFunction lossFunction,
                               int variables,
                               int populationSize,
                               int minValue,
                               int maxValue,
                               double mutationChance,
                               int generations) {
        this.lossFunction = lossFunction;
        this.variablesNumber = variables;
        this.populationSize = populationSize;
        this.minValue = minValue;
        this.maxValue = maxValue;
        this.mutationChance = mutationChance;
        this.generations = generations;
    }

    protected List<Solution> createInitialPopulation() {
        List<Solution> population = new ArrayList<>(populationSize);
        for (int i = 0; i < populationSize; i++) {
            population.add(Solution.randomVector(minValue, maxValue, variablesNumber));
        }
        return population;
    }

    protected Solution mutate(Solution solution) {
        return solution.map(v -> Common.random.nextDouble() > mutationChance ?
                v : Common.random.nextDouble(minValue, maxValue));
    }

    protected Solution bestSolution(List<Solution> population) {
        return population.stream()
                .min(Comparator.comparing(lossFunction::valueAt))
                .orElseThrow();
    }

    protected Solution cross(Solution firstParent, Solution secondParent) {
        Solution child = new Solution(new ArrayRealVector(variablesNumber));

        for (int i = 0; i < child.getDimension(); i++) {
            double valParent1 = firstParent.getEntry(i);
            double valParent2 = secondParent.getEntry(i);


            child.setEntry(i, Common.random.nextBoolean() ? valParent1 : valParent2);
        }

        return child;
    }

    protected List<Solution> selectByRouletteWheel(List<Solution> population, int solutionsToSelect) {
        double[] cumulativeFitness = new double[populationSize];
        cumulativeFitness[0] = lossFunction.valueAt(population.get(0));

        for (int i = 1; i < populationSize; i++) {
            cumulativeFitness[i] = cumulativeFitness[i - 1] + lossFunction.valueAt(population.get(i));
        }

        List<Solution> selection = new ArrayList<>();
        for (int i = 0; i < solutionsToSelect; i++) {
            double randomFitness = Common.random.nextDouble() * cumulativeFitness[populationSize - 1];
            int index = Arrays.binarySearch(cumulativeFitness, randomFitness);
            if (index < 0) index = Math.abs(index + 1);

            selection.add(population.get(index));
        }

        return selection;
    }

}
