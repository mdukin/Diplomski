package hr.fer.mekrac.fuzzy.control.fuzzyfication;

import hr.fer.mekrac.fuzzy.set.IFuzzySet;

/**
 * @author matejc
 * Created on 09.11.2022.
 */

public class COADefuzzifier implements IDefuzzifier {
    @Override
    public int deFuzzify(IFuzzySet fuzzySet) {
        if (fuzzySet.getDomain().getNumberOfComponents() != 1) throw new IllegalArgumentException("1D domain required");

        double centroidArea = 0;
        double area = 0;

        for (var el : fuzzySet.getDomain()) {
            centroidArea += fuzzySet.getValueAt(el) * el.getComponentValue(0);
            area += fuzzySet.getValueAt(el);
        }
        return Math.toIntExact(Math.round(centroidArea / area));
    }
}
