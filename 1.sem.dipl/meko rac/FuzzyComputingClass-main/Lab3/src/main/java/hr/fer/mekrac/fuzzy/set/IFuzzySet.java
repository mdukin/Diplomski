package hr.fer.mekrac.fuzzy.set;

import hr.fer.mekrac.fuzzy.domain.DomainElement;
import hr.fer.mekrac.fuzzy.domain.IDomain;

/**
 * @author matejc
 * Created on 13.10.2022.
 */

public interface IFuzzySet {
    IDomain getDomain();

    double getValueAt(DomainElement domainElement);
}
