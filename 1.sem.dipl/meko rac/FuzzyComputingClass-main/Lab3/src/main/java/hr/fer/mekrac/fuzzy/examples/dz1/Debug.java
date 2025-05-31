package hr.fer.mekrac.fuzzy.examples.dz1;

import hr.fer.mekrac.fuzzy.set.IFuzzySet;
import hr.fer.mekrac.fuzzy.domain.DomainElement;
import hr.fer.mekrac.fuzzy.domain.IDomain;

/**
 * @author matejc
 * Created on 13.10.2022.
 */

public class Debug {

    private Debug() {

    }

    public static void print(IDomain domain, String headingText) {

        if (headingText != null) {
            System.out.println(headingText);
        }
        for (DomainElement e : domain) {

            System.out.println("Element domene: " + e);
        }
        System.out.println("Kardinalitet domene je: " + domain.getCardinality());
        System.out.println();

    }

    public static void print(IFuzzySet fuzzySet, String headingText) {
        if (headingText != null) {
            System.out.println(headingText);
        }

        fuzzySet.getDomain().iterator().forEachRemaining(domainElement ->
                System.out.printf("d%s=%5f%n", domainElement, fuzzySet.getValueAt(domainElement)));
        System.out.println();
    }
}
