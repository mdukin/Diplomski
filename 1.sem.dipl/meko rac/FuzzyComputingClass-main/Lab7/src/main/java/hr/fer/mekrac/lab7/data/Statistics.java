package hr.fer.mekrac.lab7.data;

import hr.fer.mekrac.lab7.network.NeuralNetwork;
import hr.fer.mekrac.lab7.objective.IObjectiveFunction;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @author matejc
 * Created on 13.01.2023.
 */

public class Statistics {
    private Statistics() {
    }

    public static String getStatistics(NeuralNetwork network, Dataset dataset, IObjectiveFunction objectiveFunction) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < dataset.size(); i++) {
            var inputs = dataset.getInputsAtIndex(i);
            var outputs = dataset.getOutputsAtIndex(i);

            var predictedRaw = network.calcOutput(inputs);
            var predicted = Arrays.stream(predictedRaw)
                    .mapToInt(x -> x < 0.5 ? 0 : 1)
                    .toArray();

            sb.append(
                    Arrays.stream(inputs)
                            .mapToObj(x -> String.format("%.3f", x))
                            .collect(Collectors.joining("\t"))
            ).append("\t").append(
                    Arrays.stream(outputs)
                            .mapToObj(Integer::toString)
                            .collect(Collectors.joining("\t"))
            ).append("\t\t").append(
                    Arrays.stream(predicted)
                            .mapToObj(Integer::toString)
                            .collect(Collectors.joining("\t"))
            ).append("\n");
        }
        sb.append("MSE: ").append(objectiveFunction.valueAt(network)).append("\n");
        sb.append("Accuracy: ").append(getAccuracy(network, dataset)).append("%\n");


        return sb.toString();
    }

    private static double getAccuracy(NeuralNetwork network, Dataset dataset) {
        double accSum = 0;

        for (int i = 0; i < dataset.size(); i++) {
            var inputs = dataset.getInputsAtIndex(i);
            var outputs = dataset.getOutputsAtIndex(i);

            var predictedRaw = network.calcOutput(inputs);
            var predicted = Arrays.stream(predictedRaw)
                    .mapToInt(x -> x < 0.5 ? 0 : 1)
                    .toArray();

            if (Arrays.equals(predicted, outputs))
                accSum += 1;

        }
        return accSum / dataset.size();
    }

    public static String getWeights(NeuralNetwork solution) {
        return Arrays.stream(solution.getParameters())
                .mapToObj(x -> String.format("%.4f", x))
                .collect(Collectors.joining(",", "[", "]"));
    }

    public static String printTypeOneNeuronMemory(NeuralNetwork solution) {
        StringBuilder sb = new StringBuilder();

        int paramIndex = 0;
        for (int i = 0; i < solution.getStructure()[1]; i++) {

            List<Double> weights = new ArrayList<>();
            List<Double> sList = new ArrayList<>();

            for (int j = 0; j < solution.getStructure()[0]; j++) {
                double w = solution.getParameters()[paramIndex];
                double s = solution.getParameters()[paramIndex + 1];

                weights.add(w);
                sList.add(s);
                paramIndex += 2;
            }

            sb.append(
                    weights.stream()
                            .map(x -> String.format("%.3f", x))
                            .collect(Collectors.joining(",", "(", ")"))
            ).append(
                    "\t"
            ).append(
                    sList.stream()
                            .map(x -> String.format("%.3f", x))
                            .collect(Collectors.joining(",", "{", "}"))
            ).append("\n");
        }

        return sb.toString();
    }
}
