package ga.function;

import ga.data.Reading;
import ga.data.Solution;

import java.util.HashMap;
import java.util.List;

/**
 * @author matejc
 * Created on 14.11.2022.
 */

public class MeanSquareLossFunction {
    private final List<Reading> readings;
    private HashMap<Solution, Double> cache;

    public MeanSquareLossFunction(List<Reading> readings) {
        this.readings = readings;

        initCache();
    }

    public void initCache() {
        this.cache = new HashMap<>(readings.size());
    }

    public double valueAt(Solution point) {
        return cache.computeIfAbsent(point, k -> readings.stream()
                .mapToDouble(reading -> TransferFunction.valueAt(reading.x(), reading.y(), reading.fOut(), point))
                .map(x -> x * x)
                .average().orElse(Double.MAX_VALUE));
    }

}
