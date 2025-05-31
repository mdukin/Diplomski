package hr.fer.mekrac.lab7.mutation;

/**
 * @author matejc
 * Created on 13.01.2023.
 */

@FunctionalInterface
public interface IMutation {
    void mutate(double[] parameters);
}
