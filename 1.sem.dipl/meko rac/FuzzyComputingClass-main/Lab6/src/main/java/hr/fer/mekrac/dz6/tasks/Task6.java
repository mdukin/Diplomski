package hr.fer.mekrac.dz6.tasks;

import hr.fer.mekrac.dz6.Sample;
import hr.fer.mekrac.dz6.SampleFactory;
import hr.fer.mekrac.dz6.network.AnfisNetwork;
import hr.fer.mekrac.dz6.output.OutputWriter;

/**
 * @author matejc
 * Created on 28.12.2022.
 */

public class Task6 {
    private static final int BATCH_SIZE = 9;
    private static final double LEARNING_RATE = 5E-4;
    private static final int RULES = 6;

    public static void main(String[] args) {
        var samples = SampleFactory.sampleFunction(SampleFactory.LAB_FUNCTION, -4, 4, -4, 4);


        AnfisNetwork anfisNetwork = new AnfisNetwork(RULES, BATCH_SIZE);
        anfisNetwork.train(samples, 10_000, LEARNING_RATE);

        var output = samples.stream()
                .map(sample ->
                        new Sample(sample.x(), sample.y(),
                                sample.z() - anfisNetwork.predict(sample.x(), sample.y())))
                .toList();

        OutputWriter.writeSamplesToFile("task6.txt", output);
    }
}
