package hr.fer.mekrac.fuzzy.control.system;

import hr.fer.mekrac.fuzzy.control.fuzzyfication.IDefuzzifier;
import hr.fer.mekrac.fuzzy.control.reading.CrispInputReading;
import hr.fer.mekrac.fuzzy.math.IBinaryFunction;
import hr.fer.mekrac.fuzzy.math.Operations;
import hr.fer.mekrac.fuzzy.rule.Rule;
import hr.fer.mekrac.fuzzy.set.IFuzzySet;

import java.util.Collection;
import java.util.List;

/**
 * @author matejc
 * Created on 09.11.2022.
 */

public abstract class FuzzySystem {

    private final IDefuzzifier defuzzifier;
    private final FuzzySystemSetting fuzzySystemSetting;

    protected FuzzySystem(IDefuzzifier defuzzifier, FuzzySystemSetting fuzzySystemSetting) {
        this.defuzzifier = defuzzifier;
        this.fuzzySystemSetting = fuzzySystemSetting;
    }

    private IBinaryFunction getTNorm() {
        return fuzzySystemSetting == FuzzySystemSetting.MINIMUM
                ? Operations.zadehAnd() : Operations.product;
    }

    private IBinaryFunction getSNorm() {
        return Operations.zadehOr();
    }

    public abstract List<Rule> getFuzzySystemRules();

    public int decide(CrispInputReading crispInputReading) {
        IFuzzySet result = generateResultSet(crispInputReading, getFuzzySystemRules());

        return defuzzifier.deFuzzify(result);
    }

    public IFuzzySet generateResultSet(CrispInputReading crispInputReading, Collection<Rule> rules) {
        IFuzzySet result;

        var consequences = rules.stream()
                .map(rule -> rule.applyRule(crispInputReading, getTNorm()))
                .toList();

        result = consequences.get(0);
        for (IFuzzySet c : consequences) {
            result = Operations.binaryOperation(result, c, getSNorm());
        }
        return result;
    }

}
