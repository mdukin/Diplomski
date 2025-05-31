package hr.fer.mekrac.fuzzy.math;

import hr.fer.mekrac.fuzzy.set.IFuzzySet;
import hr.fer.mekrac.fuzzy.domain.DomainElement;
import hr.fer.mekrac.fuzzy.set.MutableFuzzySet;

/**
 * @author matejc
 * Created on 13.10.2022.
 */

public class Operations {
    private Operations() {
    }

    public static IFuzzySet unaryOperation(IFuzzySet fuzzySet, IUnaryFunction unaryFunction) {

        MutableFuzzySet mutableFuzzySet = new MutableFuzzySet(fuzzySet.getDomain());

        for (DomainElement el : fuzzySet.getDomain()) {
            mutableFuzzySet.set(el, unaryFunction.valueAt(fuzzySet.getValueAt(el)));
        }

        return mutableFuzzySet;
    }

    public static IFuzzySet binaryOperation(IFuzzySet first, IFuzzySet second, IBinaryFunction binaryFunction) {
        MutableFuzzySet mutableFuzzySet = new MutableFuzzySet(first.getDomain());

        for (DomainElement el : first.getDomain()) {
            mutableFuzzySet.set(el, binaryFunction.valueAt(first.getValueAt(el), second.getValueAt(el)));
        }

        return mutableFuzzySet;
    }

    public static IUnaryFunction zadehNot() {
        return x -> 1 - x;
    }

    public static IBinaryFunction zadehAnd() {
        return Math::min;
    }

    public static IBinaryFunction zadehOr() {
        return Math::max;
    }

    public static final IBinaryFunction product = (a, b) -> a * b;

    public static IBinaryFunction hamacherTNorm(double v) {
        return (a, b) -> (a * b) / (v + (1 - v) * (a + b - a * b));
    }

    public static IBinaryFunction hamacherSNorm(double v) {
        return (a, b) -> (a + b - (2 - v) * a * b) / (1 - (1 - v) * a * b);
    }
}
