package hr.fer.mekrac.fuzzy.control.reading;

import hr.fer.mekrac.fuzzy.set.IFuzzySet;

/**
 * @author matejc
 * Created on 10.11.2022.
 */

public record ShipAntecedentSet(
        IFuzzySet left,
        IFuzzySet right,
        IFuzzySet leftAngle,
        IFuzzySet rightAngle,
        IFuzzySet speed,
        IFuzzySet rightPath,
        int populatedSets
) {
    public IFuzzySet[] getSetsAsArray() {
        return new IFuzzySet[]{left, right, leftAngle, rightAngle, speed, rightPath};
    }

}
