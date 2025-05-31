package hr.fer.mekrac.fuzzy.domain;

import java.util.Arrays;
import java.util.stream.Collectors;

/**
 * @author matejc
 * Created on 12.10.2022.
 */

public class DomainElement {
    private final int[] values;

    public DomainElement(int[] values) {
        this.values = values.clone();
    }

    public int getNumberOfComponents() {
        return values.length;
    }

    public int getComponentValue(int index) {
        return values[index];
    }

    int[] getValues() {
        return values;
    }

    @Override
    public String toString() {
        return Arrays.stream(values)
                .mapToObj(String::valueOf)
                .collect(Collectors.joining(",", "(", ")"));
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        DomainElement that = (DomainElement) o;

        return Arrays.equals(values, that.values);
    }

    @Override
    public int hashCode() {
        return Arrays.hashCode(values);
    }

    public static DomainElement of(int... array) {
        return new DomainElement(array);
    }
}
