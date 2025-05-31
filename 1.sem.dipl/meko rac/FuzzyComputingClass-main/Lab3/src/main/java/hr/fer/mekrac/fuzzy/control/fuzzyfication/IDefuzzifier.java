package hr.fer.mekrac.fuzzy.control.fuzzyfication;

import hr.fer.mekrac.fuzzy.set.IFuzzySet;

/**
 * @author matejc
 * Created on 09.11.2022.
 */

@FunctionalInterface
public interface IDefuzzifier {
    int deFuzzify(IFuzzySet fuzzySet);
}
