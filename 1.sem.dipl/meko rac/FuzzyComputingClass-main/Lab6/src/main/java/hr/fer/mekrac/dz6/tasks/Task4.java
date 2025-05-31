package hr.fer.mekrac.dz6.tasks;

import hr.fer.mekrac.dz6.Sample;
import hr.fer.mekrac.dz6.SampleFactory;
import hr.fer.mekrac.dz6.network.AnfisNetwork;
import hr.fer.mekrac.dz6.output.OutputWriter;

import java.util.List;

/**
 * @author matejc
 * Created on 28.12.2022.
 */

public class Task4 {

    private static final int BATCH_SIZE = 9;
    private static final double LEARNING_RATE = 1E-4;

    public static void main(String[] args) {
        List<Integer> rules = List.of(1, 2, 6);
        var samples = SampleFactory.sampleFunction(SampleFactory.LAB_FUNCTION, -4, 4, -4, 4);


        for (var rule : rules) {
            AnfisNetwork anfisNetwork = new AnfisNetwork(rule, BATCH_SIZE);
            anfisNetwork.train(samples, 10_000, LEARNING_RATE);

            var output = samples.stream()
                    .map(sample ->
                            new Sample(sample.x(), sample.y(),
                                    anfisNetwork.predict(sample.x(), sample.y())))
                    .toList();

            OutputWriter.writeSamplesToFile("task4-%d.txt".formatted(rule), output);
        }
    }
}
