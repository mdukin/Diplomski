package hr.fer.mekrac.lab7.mutation;

import java.util.Arrays;
import java.util.List;

import static hr.fer.mekrac.lab7.util.Common.RANDOM;

/**
 * @author matejc
 * Created on 13.01.2023.
 */

public class CombinedMutation implements IMutation {
    private final List<IMutation> mutations;
    private final double[] frequencies;
    private final double sum;

    public CombinedMutation(double[] frequencies, IMutation... mutations) {
        this.mutations = Arrays.asList(mutations);
        this.frequencies = frequencies;

        this.sum = Arrays.stream(frequencies)
                .sum();
    }


    @Override
    public void mutate(double[] parameters) {
        double picked = RANDOM.nextDouble(sum);
        double current = 0;

        IMutation pickedMutation = null;

        for (int i = 0; i < mutations.size(); i++) {
            if (picked <= frequencies[i] + current) {
                pickedMutation = mutations.get(i);
                break;
            }
            current += frequencies[i];
        }

        pickedMutation.mutate(parameters);
    }
}
