package ga.data;

import ga.util.Common;
import org.apache.commons.math3.analysis.UnivariateFunction;
import org.apache.commons.math3.exception.DimensionMismatchException;
import org.apache.commons.math3.exception.NotPositiveException;
import org.apache.commons.math3.exception.OutOfRangeException;
import org.apache.commons.math3.linear.ArrayRealVector;
import org.apache.commons.math3.linear.RealVector;

import java.util.Arrays;
import java.util.stream.Collectors;

/**
 * @author matejc
 * Created on 14.11.2022.
 */

public class Solution extends RealVector {
    protected final RealVector proxy;

    public Solution(RealVector proxy) {
        this.proxy = proxy;
    }

    public static Solution randomVector(double pointRangeLower, double pointRangeHigher, int variables) {
        if (pointRangeLower > pointRangeHigher) throw new IllegalArgumentException("Min is larger than max");

        RealVector vector = new ArrayRealVector(variables);

        for (int i = 0; i < variables; i++) {
            vector.setEntry(i, Common.random.nextDouble(pointRangeLower, pointRangeHigher));
        }

        return new Solution(vector);
    }

    @Override
    public String toString() {
        return Arrays.stream(proxy.toArray())
                .mapToObj(val -> String.format("%.3f", val))
                .collect(Collectors.joining(", ", "(", ")"));
    }

    @Override
    public int getDimension() {
        return proxy.getDimension();
    }

    @Override
    public double getEntry(int index) throws OutOfRangeException {
        return proxy.getEntry(index);
    }

    @Override
    public void setEntry(int index, double value) throws OutOfRangeException {
        proxy.setEntry(index, value);
    }

    @Override
    public RealVector append(RealVector v) {
        return proxy.append(v);
    }

    @Override
    public RealVector append(double d) {
        return proxy.append(d);
    }

    @Override
    public RealVector getSubVector(int index, int n) throws NotPositiveException, OutOfRangeException {
        return proxy.getSubVector(index, n);
    }

    @Override
    public void setSubVector(int index, RealVector v) throws OutOfRangeException {
        proxy.setSubVector(index, v);
    }

    @Override
    public boolean isNaN() {
        return proxy.isNaN();
    }

    @Override
    public boolean isInfinite() {
        return proxy.isInfinite();
    }

    @Override
    public Solution copy() {
        return new Solution(proxy.copy());
    }

    @Override
    public RealVector ebeDivide(RealVector v) throws DimensionMismatchException {
        return proxy.ebeDivide(v);
    }

    @Override
    public RealVector ebeMultiply(RealVector v) throws DimensionMismatchException {
        return proxy.ebeMultiply(v);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Solution that = (Solution) o;

        return proxy.equals(that.proxy);
    }

    @Override
    public int hashCode() {
        return proxy.hashCode();
    }

    @Override
    public Solution map(UnivariateFunction function) {
        return new Solution(super.map(function));
    }

    @Override
    public Solution mapAdd(double d) {
        return new Solution(proxy.mapAdd(d));
    }
}
