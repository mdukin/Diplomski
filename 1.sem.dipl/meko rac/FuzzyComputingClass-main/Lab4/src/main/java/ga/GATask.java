package ga;

import ga.algorithm.EliminationAlgorithm;
import ga.algorithm.GenerationAlgorithm;
import ga.algorithm.IAlgorithm;
import ga.data.Reading;
import ga.data.Solution;
import ga.function.MeanSquareLossFunction;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

/**
 * @author matejc
 * Created on 13.11.2022.
 */

public class GATask {

    public static final int VARIABLES = 5;
    public static final int MIN_VALUE = - 4;
    public static final int MAX_VALUE = 4;
    public static final int POPULATION_SIZE = 100;
    public static final double MUTATION_CHANCE = 0.25;
    public static final int GENERATIONS_GENERATIVE = 10_000;
    public static final int GENERATIONS_ELIMINATION = 10_000;
    public static final boolean ELITISM = true;

    public static void main(String[] args) {
        if (args.length != 2)
            throw new IllegalArgumentException("Required path of dataset and number of algorithm as argument");

        Path dataset = Path.of(args[0]);
        if (! Files.isReadable(dataset)) throw new IllegalArgumentException("Dataset can't be read");

        try {
            List<Reading> readings = loadReadings(dataset);

            MeanSquareLossFunction lossFunction = new MeanSquareLossFunction(readings);

            IAlgorithm<Solution> algorithm = switch (Integer.parseInt(args[1])) {
                case 0 -> new GenerationAlgorithm(lossFunction,
                        VARIABLES, POPULATION_SIZE,
                        MIN_VALUE, MAX_VALUE,
                        MUTATION_CHANCE,
                        GENERATIONS_GENERATIVE,
                        ELITISM);
                case 1 -> new EliminationAlgorithm(lossFunction,
                        VARIABLES, POPULATION_SIZE,
                        MIN_VALUE, MAX_VALUE,
                        GENERATIONS_ELIMINATION,
                        MUTATION_CHANCE);
                default -> throw new IllegalArgumentException("No such argument");
            };

            Solution solution = algorithm.run();

            System.out.printf("Solution found: %s.%n", solution);
            System.out.printf("Loss function value of solution = %f.%n", lossFunction.valueAt(solution));

        } catch (IOException e) {
            System.err.printf("Error reading file %s.%n", e.getMessage());
            System.exit(- 1);
        }

    }

    private static List<Reading> loadReadings(Path dataset) throws IOException {
        try (var buf = Files.newBufferedReader(dataset)) {
            return buf.lines()
                    .map(Reading::parseReading).toList();
        }
    }
}
