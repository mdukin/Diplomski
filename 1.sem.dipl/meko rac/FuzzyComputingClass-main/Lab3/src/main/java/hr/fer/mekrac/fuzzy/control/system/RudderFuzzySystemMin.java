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

public class RudderFuzzySystemMin extends FuzzySystem {
    public RudderFuzzySystemMin(IDefuzzifier defuzzifier, FuzzySystemSetting fuzzySystemSetting) {
        super(defuzzifier, fuzzySystemSetting);
    }

    @Override
    public List<Rule> getFuzzySystemRules() {
        return List.of(
                new Rule(new ShipAntecedentSet(null,
                        null,
                        VERY_CLOSE_TO_LAND,
                        null,
                        null,
                        null,
                        1),
                        RIGHT_TURN_HARD),
                new Rule(new ShipAntecedentSet(null,
                        null,
                        null,
                        VERY_CLOSE_TO_LAND,
                        null,
                        null,
                        1),
                        LEFT_TURN_HARD),
                new Rule(new ShipAntecedentSet(CLOSE_TO_LAND,
                        null,
                        CLOSE_TO_LAND,
                        null,
                        null,
                        null,
                        2),
                        RIGHT_TURN_SOFT),
                new Rule(new ShipAntecedentSet(null,
                        CLOSE_TO_LAND,
                        null,
                        CLOSE_TO_LAND,
                        null,
                        null,
                        2),
                        LEFT_TURN_SOFT),
                new Rule(new ShipAntecedentSet(null,
                        null,
                        null,
                        null,
                        null,
                        WRONG_PATH,
                        1),
                        RIGHT_TURN_HARD)
        );
    }
}
