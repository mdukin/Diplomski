package hr.fer.mekrac.fuzzy.control.system;

import hr.fer.mekrac.fuzzy.control.fuzzyfication.IDefuzzifier;
import hr.fer.mekrac.fuzzy.control.reading.ShipAntecedentSet;
import hr.fer.mekrac.fuzzy.rule.Rule;

import java.util.List;

import static hr.fer.mekrac.fuzzy.ship.ShipSets.*;

/**
 * @author matejc
 * Created on 09.11.2022.
 */

public class AccelerationFuzzySystemMin extends FuzzySystem {

    public AccelerationFuzzySystemMin(IDefuzzifier defuzzifier, FuzzySystemSetting fuzzySystemSetting) {
        super(defuzzifier, fuzzySystemSetting);
    }

    @Override
    public List<Rule> getFuzzySystemRules() {
        return List.of(
                new Rule(new ShipAntecedentSet(null,
                        null,
                        null,
                        null,
                        SLOW,
                        null,
                        1),
                        ACCELERATE),
                new Rule(new ShipAntecedentSet(null,
                        null,
                        null,
                        null,
                        FAST,
                        null,
                        1),
                        DECELERATE),
                new Rule(new ShipAntecedentSet(CLOSE_TO_LAND,
                        null,
                        CLOSE_TO_LAND,
                        null,
                        null,
                        null,
                        2),
                        DECELERATE),
                new Rule(new ShipAntecedentSet(null,
                        CLOSE_TO_LAND,
                        null,
                        CLOSE_TO_LAND,
                        null,
                        null,
                        2),
                        DECELERATE),
                new Rule(new ShipAntecedentSet(FAR_FROM_LAND,
                        FAR_FROM_LAND,
                        FAR_FROM_LAND,
                        FAR_FROM_LAND,
                        null,
                        null,
                        4),
                        ACCELERATE)
        );
    }
}
