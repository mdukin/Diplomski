package hr.fer.mekrac.dz6.network;

/**
 * @author matejc
 * Created on 28.12.2022.
 */

public class DerivationVariables {
    final double[] alpha;
    final double[] beta;
    final double[] pi;
    final double[] z;
    final double[] dA;
    final double[] dB;
    final double[] dC;
    final double[] dD;
    final double[] dP;
    final double[] dR;
    final double[] dQ;

    public DerivationVariables(int numberOfVariables) {
        alpha = new double[numberOfVariables];
        beta = new double[numberOfVariables];
        pi = new double[numberOfVariables];
        z = new double[numberOfVariables];
        dA = new double[numberOfVariables];
        dB = new double[numberOfVariables];
        dC = new double[numberOfVariables];
        dD = new double[numberOfVariables];
        dP = new double[numberOfVariables];
        dR = new double[numberOfVariables];
        dQ = new double[numberOfVariables];
    }
}
