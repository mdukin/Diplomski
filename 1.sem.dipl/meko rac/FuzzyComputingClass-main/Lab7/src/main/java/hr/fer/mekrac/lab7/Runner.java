package hr.fer.mekrac.lab7;

import hr.fer.mekrac.lab7.crossover.*;
import hr.fer.mekrac.lab7.data.Dataset;
import hr.fer.mekrac.lab7.data.Statistics;
import hr.fer.mekrac.lab7.evolution.GenerationEvolutionAlgorithm;
import hr.fer.mekrac.lab7.evolution.IAlgorithm;
import hr.fer.mekrac.lab7.mutation.CombinedMutation;
import hr.fer.mekrac.lab7.mutation.GaussianAddMutation;
import hr.fer.mekrac.lab7.mutation.GaussianReplaceMutation;
import hr.fer.mekrac.lab7.mutation.IMutation;
import hr.fer.mekrac.lab7.network.NeuralNetwork;
import hr.fer.mekrac.lab7.objective.IObjectiveFunction;
import hr.fer.mekrac.lab7.objective.MSEFunction;
import hr.fer.mekrac.lab7.selection.ISelectionAlgorithm;
import hr.fer.mekrac.lab7.selection.ITournamentSelection;

import java.io.IOException;
import java.nio.file.Path;

public class Runner {

    private static final int[] STRUCTURE = {2, 8, 3};
    private static final int POPULATION = 20;
    private static final int GENERATIONS = 100_000;
    private static final double MIN_ERROR = 10E-7;

    private static final double PROB1 = 0.02;
    private static final double STDDEV1 = 0.5;
    private static final double PROB2 = 0.05;
    private static final double STDDEV2 = 0.05;
    private static final double PROB3 = 0.005;
    private static final double STDDEV3 = 4.0;
    private static final double[] mutationAlgFrequencies = {1, 2, 0.5};

    private static final double BLX_ALPHA = 0.5;
    private static final double INIT_STDDEV = 2.0;
    private static final int TOURNAMENT_SIZE = 4;


    public static void main(String[] args) {
        if (args.length != 1) throw new IllegalArgumentException("Path of dataset required as argument.");

        Path datasetPath = Path.of(args[0]);

        IMutation mutation = new CombinedMutation(mutationAlgFrequencies,
                new GaussianAddMutation(PROB1, STDDEV1),
                new GaussianAddMutation(PROB2, STDDEV2),
                new GaussianReplaceMutation(PROB3, STDDEV3));

        ICrossover crossover = new CombinedCrossover(
                new ArithmeticCrossover(),
                new UniformCrossover(),
                new BLXCrossover(BLX_ALPHA)
        );

        try {
            Dataset dataset = Dataset.read(datasetPath);

            IObjectiveFunction objectiveFunction = new MSEFunction(dataset);

            ISelectionAlgorithm selectionAlgorithm = new ITournamentSelection(TOURNAMENT_SIZE);

            IAlgorithm algorithm = new GenerationEvolutionAlgorithm(STRUCTURE,
                    POPULATION,
                    GENERATIONS,
                    MIN_ERROR,
                    INIT_STDDEV,
                    mutation,
                    crossover,
                    objectiveFunction,
                    selectionAlgorithm);

            NeuralNetwork solution = algorithm.run();

            System.out.println(Statistics.getStatistics(solution, dataset, objectiveFunction));
            System.out.println(Statistics.getWeights(solution));
            System.out.println(Statistics.printTypeOneNeuronMemory(solution));

        } catch (IOException e) {
            e.printStackTrace();
            System.err.println(e.getMessage());

            System.exit(-1);
        }
    }
}