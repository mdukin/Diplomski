package hr.fer.mekrac.lab7.objective;

import hr.fer.mekrac.lab7.data.Dataset;
import hr.fer.mekrac.lab7.network.NeuralNetwork;
import lombok.RequiredArgsConstructor;

/**
 * @author matejc
 * Created on 13.01.2023.
 */

@RequiredArgsConstructor
public class MSEFunction implements IObjectiveFunction {

    private final Dataset dataset;

    @Override
    public double valueAt(NeuralNetwork network) {
        double mseSum = 0;

        for (int i = 0; i < dataset.size(); i++) {
            var inputs = dataset.getInputsAtIndex(i);
            var outputsTrue = dataset.getOutputsAtIndex(i);

            var calculatedOutputs = network.calcOutput(inputs);

            for (int j = 0; j < outputsTrue.length; j++) {
                mseSum += Math.pow(calculatedOutputs[j] - outputsTrue[j], 2);
            }
        }
        return mseSum / dataset.size();
    }
}
