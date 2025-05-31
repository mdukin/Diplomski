package hr.fer.mekrac.lab7.selection;

import hr.fer.mekrac.lab7.network.NeuralNetwork;
import hr.fer.mekrac.lab7.util.Common;
import lombok.RequiredArgsConstructor;

import java.util.*;

/**
 * @author matejc
 * Created on 14.01.2023.
 */

@RequiredArgsConstructor
public class ITournamentSelection implements ISelectionAlgorithm {

    private final int tournamentSize;

    @Override
    public List<NeuralNetwork> selectFromPopulation(List<NeuralNetwork> population, double[] errors, int n) {
        List<NeuralNetwork> selection = new ArrayList<>();

        while (selection.size() != n) {
            NeuralNetwork pick = pickOneWithTournament(population, errors);
            if (!selection.contains(pick)) {
                selection.add(pick);
            }
        }

        return selection;
    }

    private NeuralNetwork pickOneWithTournament(List<NeuralNetwork> population, double[] errors) {
        Set<Integer> randomIndexes = new HashSet<>();
        while (randomIndexes.size() != tournamentSize) {
            int index = Common.RANDOM.nextInt(population.size());
            randomIndexes.add(index);
        }

        int winnerIndex = randomIndexes.stream()
                .min(Comparator.comparingDouble(index -> errors[index]))
                .orElseThrow();

        return population.get(winnerIndex);
    }
}
