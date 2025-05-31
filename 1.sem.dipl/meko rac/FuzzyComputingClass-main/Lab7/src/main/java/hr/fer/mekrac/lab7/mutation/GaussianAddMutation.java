package hr.fer.mekrac.lab7.mutation;

import lombok.RequiredArgsConstructor;

import static hr.fer.mekrac.lab7.util.Common.RANDOM;

/**
 * @author matejc
 * Created on 13.01.2023.
 */

@RequiredArgsConstructor
public class GaussianAddMutation implements IMutation {

    private final double probability;
    private final double stddev;

    @Override
    public void mutate(double[] parameters) {
        for (int i = 0; i < parameters.length; i++) {
            if (RANDOM.nextDouble()<=probability) {
                parameters[i] += RANDOM.nextGaussian(0, stddev);
            }
        }
    }
}
