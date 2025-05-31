package hr.fer.mekrac.fuzzy.rule;

import hr.fer.mekrac.fuzzy.control.reading.CrispInputReading;
import hr.fer.mekrac.fuzzy.control.reading.ShipAntecedentSet;
import hr.fer.mekrac.fuzzy.domain.DomainElement;
import hr.fer.mekrac.fuzzy.math.IBinaryFunction;
import hr.fer.mekrac.fuzzy.math.Operations;
import hr.fer.mekrac.fuzzy.set.IFuzzySet;

import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * @author matejc
 * Created on 09.11.2022.
 */

public class Rule {
    private final ShipAntecedentSet antecedent;
    private final IFuzzySet consequence;

    public Rule(ShipAntecedentSet antecedent, IFuzzySet consequence) {
        this.antecedent = antecedent;
        this.consequence = consequence;
    }

    public IFuzzySet applyRule(CrispInputReading inputReading, IBinaryFunction tNorm) {
        double alpha = 1;

        var iterator = new AntecedentApplyIterator(inputReading);

        while (iterator.hasNext()) {
            alpha = tNorm.valueAt(alpha, iterator.next());
        }

        double finalAlpha = alpha;
        return Operations.unaryOperation(consequence, v -> tNorm.valueAt(v, finalAlpha));
    }


    private class AntecedentApplyIterator implements Iterator<Double> {

        private final int[] inputReadingsArray;
        private final IFuzzySet[] antecedentArray;
        private int i = 0;
        private int counter = 0;

        public AntecedentApplyIterator(CrispInputReading inputReading) {
            this.inputReadingsArray = inputReading.getValuesAsArray();
            this.antecedentArray = antecedent.getSetsAsArray();
        }

        @Override
        public boolean hasNext() {
            return counter < antecedent.populatedSets();
        }

        @Override
        public Double next() {
            if (! hasNext()) {
                throw new NoSuchElementException();
            }

            IFuzzySet set;
            int reading;
            do {
                set = antecedentArray[i];
                reading = inputReadingsArray[i];

                i++;
            } while (set == null);
            counter += 1;

            return set.getValueAt(DomainElement.of(reading));
        }
    }
}
