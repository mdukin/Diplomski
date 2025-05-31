package hr.fer.mekrac.fuzzy.set;

import hr.fer.mekrac.fuzzy.domain.IDomain;
import hr.fer.mekrac.fuzzy.domain.DomainElement;

/**
 * @author matejc
 * Created on 13.10.2022.
 */

public class CalculatedFuzzySet implements IFuzzySet {

    private final IDomain domain;
    private final IIntUnaryFunction function;


    public CalculatedFuzzySet(IDomain domain, IIntUnaryFunction function) {
        this.domain = domain;
        this.function = function;
    }

    @Override
    public IDomain getDomain() {
        return domain;
    }

    @Override
    public double getValueAt(DomainElement domainElement) {
        return function.valueAt(domain.indexOfElement(domainElement));
    }
}
