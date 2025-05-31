package hr.fer.mekrac.fuzzy.set;

import hr.fer.mekrac.fuzzy.domain.IDomain;
import hr.fer.mekrac.fuzzy.domain.DomainElement;

/**
 * @author matejc
 * Created on 13.10.2022.
 */

public class MutableFuzzySet implements IFuzzySet {

    private final double[] memberships;

    private final IDomain domain;

    public MutableFuzzySet(IDomain domain) {
        this.domain = domain;
        memberships = new double[domain.getCardinality()];
    }

    @Override
    public IDomain getDomain() {
        return domain;
    }

    @Override
    public double getValueAt(DomainElement domainElement) {
        return memberships[domain.indexOfElement(domainElement)];
    }

    public MutableFuzzySet set(DomainElement domainElement, double mu) {
        memberships[domain.indexOfElement(domainElement)] = mu;
        return this;
    }
}
