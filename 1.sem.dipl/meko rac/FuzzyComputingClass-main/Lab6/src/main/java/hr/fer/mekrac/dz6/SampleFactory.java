package hr.fer.mekrac.dz6;

import java.util.ArrayList;
import java.util.List;

import static java.lang.Math.cos;
import static java.lang.Math.pow;

/**
 * @author matejc
 * Created on 28.12.2022.
 */

public class SampleFactory {


    public static final TwoVariableFunction LAB_FUNCTION = (x, y) ->
            (pow(x - 1, 2) + pow(y + 2, 2) - 5 * x * y + 3) * pow(cos(x / 5), 2);

    private SampleFactory() {
    }

    public static List<Sample> sampleFunction(TwoVariableFunction twoVariableFunction, int xBottomLimit, int xTopLimit,
                                              int yBottomLimit, int yTopLimit) {
        List<Sample> samples = new ArrayList<>();

        for (int x = xBottomLimit; x <= xTopLimit; x++) {
            for (int y = yBottomLimit; y <= yTopLimit; y++) {
                samples.add(new Sample(x, y, twoVariableFunction.calculate(x, y)));
            }
        }

        return samples;
    }
}
