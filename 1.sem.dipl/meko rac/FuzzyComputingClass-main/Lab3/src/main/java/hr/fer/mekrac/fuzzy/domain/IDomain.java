package hr.fer.mekrac.fuzzy.domain;

/**
 * @author matejc
 * Created on 12.10.2022.
 */

public interface IDomain extends Iterable<DomainElement> {
    int getCardinality();

    IDomain getComponent(int index);

    int getNumberOfComponents();

    int indexOfElement(DomainElement element);

    DomainElement elementForIndex(int index);
}
