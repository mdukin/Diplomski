package ga.function;

import org.apache.commons.math3.linear.RealVector;

/**
 * @author matejc
 * Created on 14.11.2022.
 */

public class TransferFunction {
    private TransferFunction() {
    }

    public static double valueAt(double x, double y, double target, RealVector point) {
        double b0 = point.getEntry(0);
        double b1 = point.getEntry(1);
        double b2 = point.getEntry(2);
        double b3 = point.getEntry(3);
        double b4 = point.getEntry(4);

        return Math.sin(b0 + b1 * x) + b2 * Math.cos(x * (b3 + y)) * 1 / (1 + Math.exp(Math.pow(x - b4, 2)))
               - target;
    }
}
