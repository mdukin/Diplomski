package hr.fer.mekrac.fuzzy.examples.dz1;

import hr.fer.mekrac.fuzzy.domain.Domain;
import hr.fer.mekrac.fuzzy.domain.IDomain;
import hr.fer.mekrac.fuzzy.math.Operations;
import hr.fer.mekrac.fuzzy.set.IFuzzySet;
import hr.fer.mekrac.fuzzy.set.MutableFuzzySet;
import hr.fer.mekrac.fuzzy.domain.DomainElement;

/**
 * @author matejc
 * Created on 13.10.2022.
 */

@SuppressWarnings("DuplicatedCode")
public class Primjer2 {

    public static void main(String[] args) {
        IDomain d = Domain.intRange(0, 11);

        IFuzzySet set1 = new MutableFuzzySet(d).set(DomainElement.of(0), 1.0).set(DomainElement.of(1), 0.8).set(DomainElement.of(2), 0.6).set(DomainElement.of(3), 0.4).set(DomainElement.of(4), 0.2);
        Debug.print(set1, "Set1:");

        IFuzzySet notSet1 = Operations.unaryOperation(set1, Operations.zadehNot());
        Debug.print(notSet1, "notSet1:");

        IFuzzySet union = Operations.binaryOperation(set1, notSet1, Operations.zadehOr());
        Debug.print(union, "Set1 union notSet1:");

        IFuzzySet hinters = Operations.binaryOperation(set1, notSet1, Operations.hamacherTNorm(1.0));
        Debug.print(hinters, "Set1 intersection with notSet1 using parameterised Hamacher T norm with parameter 1.0:");
    }

}
