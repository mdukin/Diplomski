package hr.fer.mekrac.dz6;

import hr.fer.mekrac.dz6.network.AnfisNetwork;

public class Main {

    private static final int BATCH_SIZE = 9;
    private static final double LEARNING_RATE = 1E-3;

    public static void main(String[] args) {
        if (args.length != 2)
            throw new IllegalArgumentException("Required number of rules and number of iterations as params.");

        int rulesNumber = Integer.parseInt(args[0]);
        int iterationsNumber = Integer.parseInt(args[1]);

        var samples = SampleFactory.sampleFunction(SampleFactory.LAB_FUNCTION, -4, 4, -4, 4);

        AnfisNetwork anfisNetwork = new AnfisNetwork(rulesNumber, BATCH_SIZE);
        anfisNetwork.train(samples, iterationsNumber, LEARNING_RATE);

        Sample randomSample = samples.get(0);
        System.out.printf("Predicted: %.4f, actual: %.4f%n", anfisNetwork.predict(randomSample.x(),randomSample.y()), randomSample.z());
    }
}