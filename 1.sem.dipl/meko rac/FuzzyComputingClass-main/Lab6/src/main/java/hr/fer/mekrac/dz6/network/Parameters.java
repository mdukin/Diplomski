package hr.fer.mekrac.dz6.network;

import java.util.List;
import java.util.Random;

/**
 * @author matejc
 * Created on 28.12.2022.
 */

public class Parameters {

    final double[] a;
    final double[] b;
    final double[] c;
    final double[] d;

    final double[] p;
    final double[] q;
    final double[] r;
    private final Random random;

    public Parameters(int numberOfVariables, Random random) {
        this.random = random;

        a = new double[numberOfVariables];
        b = new double[numberOfVariables];
        c = new double[numberOfVariables];
        d = new double[numberOfVariables];

        p = new double[numberOfVariables];
        q = new double[numberOfVariables];
        r = new double[numberOfVariables];

        initializeVariables();
    }

    public double[] getA() {
        return a;
    }

    public double[] getB() {
        return b;
    }

    public double[] getC() {
        return c;
    }

    public double[] getD() {
        return d;
    }

    public double[] getP() {
        return p;
    }

    public double[] getQ() {
        return q;
    }

    public double[] getR() {
        return r;
    }

    private void initializeVariables() {
        for (var variable : List.of(a, b, c, d, p, q, r)) {
            for (int i = 0; i < variable.length; i++) {
                variable[i] = random.nextDouble(-1, 1);
            }
        }
    }
}
