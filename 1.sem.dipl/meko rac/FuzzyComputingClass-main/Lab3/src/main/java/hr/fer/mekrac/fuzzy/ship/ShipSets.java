package hr.fer.mekrac.fuzzy.ship;

import hr.fer.mekrac.fuzzy.domain.DomainElement;
import hr.fer.mekrac.fuzzy.domain.IDomain;
import hr.fer.mekrac.fuzzy.set.CalculatedFuzzySet;
import hr.fer.mekrac.fuzzy.set.IFuzzySet;
import hr.fer.mekrac.fuzzy.set.MutableFuzzySet;
import hr.fer.mekrac.fuzzy.set.StandardFuzzySets;

import static hr.fer.mekrac.fuzzy.ship.ShipDomains.*;

/**
 * @author matejc
 * Created on 09.11.2022.
 */

public class ShipSets {
    private ShipSets() {
    }

    public static final IFuzzySet WRONG_PATH = new MutableFuzzySet(RIGHT_PATH)
            .set(DomainElement.of(0), 1);

    public static final IFuzzySet CLOSE_TO_LAND = new CalculatedFuzzySet(DISTANCE,
            StandardFuzzySets.lFunction(40, 70));

    public static final IFuzzySet VERY_CLOSE_TO_LAND = new CalculatedFuzzySet(DISTANCE,
            StandardFuzzySets.lFunction(30, 40));

    public static final IFuzzySet FAR_FROM_LAND = new CalculatedFuzzySet(DISTANCE,
            StandardFuzzySets.gammaFunction(100, 200));

    public static final IFuzzySet ACCELERATE = new CalculatedFuzzySet(ACCELERATION,
            StandardFuzzySets.gammaFunction(getIndexOfDomain(ACCELERATION, 10), getIndexOfDomain(ACCELERATION, 30)));

    public static final IFuzzySet DECELERATE = new CalculatedFuzzySet(ACCELERATION,
            StandardFuzzySets.lFunction(getIndexOfDomain(ACCELERATION, - 45), getIndexOfDomain(ACCELERATION, - 15)));

    public static final IFuzzySet RIGHT_TURN_HARD = new CalculatedFuzzySet(ANGLE,
            StandardFuzzySets.lFunction(getIndexOfDomain(ANGLE, - 85), getIndexOfDomain(ANGLE, - 30)));

    public static final IFuzzySet LEFT_TURN_HARD = new CalculatedFuzzySet(ANGLE,
            StandardFuzzySets.gammaFunction(getIndexOfDomain(ANGLE, 30), getIndexOfDomain(ANGLE, 85)));

    public static final IFuzzySet RIGHT_TURN_SOFT = new CalculatedFuzzySet(ANGLE,
            StandardFuzzySets.lFunction(getIndexOfDomain(ANGLE, - 25), getIndexOfDomain(ANGLE, - 5)));

    public static final IFuzzySet LEFT_TURN_SOFT = new CalculatedFuzzySet(ANGLE,
            StandardFuzzySets.gammaFunction(getIndexOfDomain(ANGLE, 5), getIndexOfDomain(ANGLE, 25)));

    public static final IFuzzySet SLOW = new CalculatedFuzzySet(SPEED,
            StandardFuzzySets.lFunction(getIndexOfDomain(SPEED, 30), getIndexOfDomain(SPEED, 40)));

    public static final IFuzzySet FAST = new CalculatedFuzzySet(SPEED,
            StandardFuzzySets.gammaFunction(getIndexOfDomain(SPEED, 65), getIndexOfDomain(SPEED, 80)));

    private static int getIndexOfDomain(IDomain domain, int elem) {
        return domain.indexOfElement(DomainElement.of(elem));
    }
}
