package hr.fer.mekrac.fuzzy.examples.dz3;

import hr.fer.mekrac.fuzzy.control.fuzzyfication.COADefuzzifier;
import hr.fer.mekrac.fuzzy.control.fuzzyfication.IDefuzzifier;
import hr.fer.mekrac.fuzzy.control.reading.CrispInputReading;
import hr.fer.mekrac.fuzzy.control.system.AccelerationFuzzySystemMin;
import hr.fer.mekrac.fuzzy.control.system.FuzzySystem;
import hr.fer.mekrac.fuzzy.control.system.FuzzySystemSetting;
import hr.fer.mekrac.fuzzy.control.system.RudderFuzzySystemMin;
import hr.fer.mekrac.fuzzy.examples.dz1.Debug;
import hr.fer.mekrac.fuzzy.set.IFuzzySet;

import java.util.Collections;
import java.util.Scanner;

import static hr.fer.mekrac.fuzzy.control.FuzzyControlSystem.parseInputString;

/**
 * @author matejc
 * Created on 09.11.2022.
 */

@SuppressWarnings("DuplicatedCode")
public class RuleTest {
    public static void main(String[] args) {

        IDefuzzifier defuzzifier = new COADefuzzifier();

        try (Scanner scanner = new Scanner(System.in).useDelimiter("\\n")) {
            System.out.println("Enter 1 for rudder or 2 for acceleration");
            FuzzySystem fuzzySystem = switch (scanner.nextInt()) {
                case 1 -> new RudderFuzzySystemMin(defuzzifier, FuzzySystemSetting.MINIMUM);
                case 2 -> new AccelerationFuzzySystemMin(defuzzifier, FuzzySystemSetting.MINIMUM);
                default -> throw new IllegalArgumentException();
            };

            System.out.println("Enter rule index starting at 0");
            int ruleIndex = scanner.nextInt();

            while (scanner.hasNext()) {
                System.out.println("Enter next inputs: ");
                String line = scanner.next();
                if (line.equalsIgnoreCase("kraj")) break;


                CrispInputReading crispInputReading = parseInputString(line);

                IFuzzySet resultSet = fuzzySystem.generateResultSet(crispInputReading,
                        Collections.singleton(fuzzySystem.getFuzzySystemRules().get(ruleIndex)));

                Debug.print(resultSet, "ResultSet");

                int crispOutput = defuzzifier.deFuzzify(resultSet);

                System.out.printf("Crisp output: %d %n%n", crispOutput);
                System.out.flush();
            }
        }
    }
}
