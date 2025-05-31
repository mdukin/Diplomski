package hr.fer.mekrac.fuzzy.relations;

import hr.fer.mekrac.fuzzy.domain.Domain;
import hr.fer.mekrac.fuzzy.domain.DomainElement;
import hr.fer.mekrac.fuzzy.domain.IDomain;
import hr.fer.mekrac.fuzzy.math.IBinaryFunction;
import hr.fer.mekrac.fuzzy.math.Operations;
import hr.fer.mekrac.fuzzy.set.IFuzzySet;
import hr.fer.mekrac.fuzzy.set.MutableFuzzySet;

/**
 * @author matejc
 * Created on 16.10.2022.
 */

public class Relations {
    private Relations() {
    }

    public static boolean isSymmetric(IFuzzySet set) {
        if (! isUTimesURelation(set)) return false;

        for (var domainElement : set.getDomain()) {
            int first = domainElement.getComponentValue(0);
            int second = domainElement.getComponentValue(1);
            DomainElement switchedElement = DomainElement.of(second, first);

            if (set.getValueAt(domainElement) != set.getValueAt(switchedElement))
                return false;
        }

        return true;
    }

    public static boolean isReflexive(IFuzzySet set) {
        if (! isUTimesURelation(set)) return false;

        for (var domainElement : set.getDomain()) {
            if (domainElement.getComponentValue(0) == domainElement.getComponentValue(1)
                && set.getValueAt(domainElement) != 1)
                return false;
        }
        return true;
    }

    public static boolean isMaxMinTransitive(IFuzzySet set) {
        if (! isReflexive(set)) return false;

        for (var xy : set.getDomain()) {
            int x = xy.getComponentValue(0);
            int y = xy.getComponentValue(1);

            for (var zElements : set.getDomain().getComponent(1)) {
                var z = zElements.getComponentValue(0);

                DomainElement xz = DomainElement.of(x, z);
                DomainElement yz = DomainElement.of(y, z);

                if (set.getValueAt(xz) < Math.min(set.getValueAt(xy), set.getValueAt(yz)))
                    return false;
            }
        }
        return true;
    }

    public static IFuzzySet compositionOfBinaryRelations(IFuzzySet set1, IFuzzySet set2) {
        if (set1.getDomain().getNumberOfComponents() != 2 ||
            set2.getDomain().getNumberOfComponents() != 2)
            throw new IllegalArgumentException("Required 2 components in set.");

        var u = set1.getDomain().getComponent(0);
        var a = set1.getDomain().getComponent(1);
        var b = set2.getDomain().getComponent(0);
        var w = set2.getDomain().getComponent(1);

        if (! a.equals(b)) throw new IllegalArgumentException("Non matching domains");

        IDomain uw = Domain.combine(u, w);

        IBinaryFunction sNorm = Operations.zadehOr();
        IBinaryFunction tNorm = Operations.zadehAnd();

        MutableFuzzySet result = new MutableFuzzySet(uw);

        for (var elX : u) {
            for (var elY : w) {

                double value = 0;
                int x = elX.getComponentValue(0);
                int y = elY.getComponentValue(0);
                for (DomainElement element : a) {
                    DomainElement xy = DomainElement.of(x, element.getComponentValue(0));
                    DomainElement yz = DomainElement.of(element.getComponentValue(0), y);
                    value = sNorm.valueAt(value, tNorm.valueAt(set1.getValueAt(xy), set2.getValueAt(yz)));
                }
                result.set(DomainElement.of(x, y), value);
            }
        }
        return result;
    }

    public static boolean isFuzzyEquivalence(IFuzzySet set) {
        return isSymmetric(set) && isReflexive(set) && isMaxMinTransitive(set);
    }

    public static boolean isUTimesURelation(IFuzzySet set) {
        IDomain domain = set.getDomain();
        if (domain.getNumberOfComponents() != 2) return false;

        IDomain xDomain = domain.getComponent(0);
        IDomain yDomain = domain.getComponent(1);

        if (xDomain.getCardinality() != yDomain.getCardinality()) return false;

        var xIterator = xDomain.iterator();
        var yIterator = yDomain.iterator();

        while (xIterator.hasNext() && yIterator.hasNext()) {
            if (xIterator.next().getComponentValue(0) != yIterator.next().getComponentValue(0))
                return false;
        }

        return true;
    }
}
