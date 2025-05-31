package hr.fer.mekrac.fuzzy.set;

/**
 * @author matejc
 * Created on 13.10.2022.
 */

public class StandardFuzzySets {
    private StandardFuzzySets() {

    }

    public static IIntUnaryFunction lFunction(int alpha, int beta) {
        return value -> {
            if (value < alpha) {
                return 1;
            } else if (value < beta) {
                return 1.0 * (beta - value) / (beta - alpha);
            } else {
                return 0;
            }
        };
    }

    public static IIntUnaryFunction gammaFunction(int alpha, int beta) {
        return value -> {
            if (value < alpha) {
                return 0;
            } else if (value < beta) {
                return 1.0 * (value - alpha) / (beta - alpha);
            } else {
                return 1;
            }
        };
    }

    public static IIntUnaryFunction lambdaFunction(int alpha, int beta, int gamma) {
        return value -> {
            if (value < alpha) {
                return 0;
            } else if (value < beta) {
                return 1.0 * (value - alpha) / (beta - alpha);
            } else if (value < gamma) {
                return 1.0 * (gamma - value) / (gamma - beta);
            } else {
                return 0;
            }
        };
    }
}
