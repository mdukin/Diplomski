package hr.fer.mekrac.fuzzy.domain;

import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.NoSuchElementException;
import java.util.stream.Collectors;

/**
 * @author matejc
 * Created on 12.10.2022.
 */

public class CompositeDomain extends Domain {

    private final SimpleDomain[] components;

    public CompositeDomain(SimpleDomain[] components) {
        this.components = components;
    }

    @Override
    public int getCardinality() {
        if (components.length == 0) return 0;

        return Arrays.stream(components)
                .mapToInt(SimpleDomain::getCardinality)
                .reduce(1, (left, right) -> left * right);
    }

    @Override
    public IDomain getComponent(int index) {
        return components[index];
    }

    @Override
    public int getNumberOfComponents() {
        return components.length;
    }

    @Override
    public Iterator<DomainElement> iterator() {

        return new Iterator<>() {
            int counter = 0;
            final int max = getCardinality();

            final LinkedList<Iterator<DomainElement>> iterators = Arrays.stream(components)
                    .map(SimpleDomain::iterator)
                    .collect(Collectors.toCollection(LinkedList::new));

            final DomainElement[] current = new DomainElement[getNumberOfComponents()];


            @Override
            public boolean hasNext() {
                return counter < max;
            }

            @Override
            public DomainElement next() {
                if (! hasNext()) throw new NoSuchElementException();

                if (counter == 0) {
                    initialize();
                } else {
                    fillNext();
                }

                counter++;

                var array = Arrays.stream(current)
                        .map(DomainElement::getValues)
                        .flatMapToInt(Arrays::stream)
                        .toArray();

                return new DomainElement(array);
            }

            private void fillNext() {
                int index = getNumberOfComponents() - 1;
                while (index >= 0) {
                    if (iterators.get(index).hasNext()) {
                        current[index] = iterators.get(index).next();
                        break;
                    } else {
                        iterators.set(index, components[index].iterator());
                        current[index] = iterators.get(index).next();
                        index--;
                    }
                }
            }

            private void initialize() {
                for (int i = 0; i < getNumberOfComponents(); i++) {
                    if (current[i] == null) current[i] = iterators.get(i).next();
                }
            }
        };
    }
}
