package hr.fer.mekrac.fuzzy.domain;

import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * @author matejc
 * Created on 12.10.2022.
 */

public class SimpleDomain extends Domain {
    private final int first;
    private final int last;

    public SimpleDomain(int first, int last) {
        this.first = first;
        this.last = last;
    }

    @Override
    public int getCardinality() {
        return last - first;
    }

    @Override
    public IDomain getComponent(int index) {
        return this;
    }

    @Override
    public int getNumberOfComponents() {
        return 1;
    }

    @Override
    public Iterator<DomainElement> iterator() {
        return new Iterator<>() {
            int current = first;

            @Override
            public boolean hasNext() {
                return current < last;
            }

            @Override
            public DomainElement next() {
                if (! hasNext()) throw new NoSuchElementException();

                return new DomainElement(new int[]{current++});
            }
        };
    }
}
