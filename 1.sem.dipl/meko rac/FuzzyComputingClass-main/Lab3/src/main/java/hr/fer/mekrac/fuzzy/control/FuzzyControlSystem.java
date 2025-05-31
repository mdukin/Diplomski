package hr.fer.mekrac.fuzzy.control;

import hr.fer.mekrac.fuzzy.control.fuzzyfication.COADefuzzifier;
import hr.fer.mekrac.fuzzy.control.fuzzyfication.IDefuzzifier;
import hr.fer.mekrac.fuzzy.control.reading.CrispInputReading;
import hr.fer.mekrac.fuzzy.control.system.AccelerationFuzzySystemMin;
import hr.fer.mekrac.fuzzy.control.system.FuzzySystem;
import hr.fer.mekrac.fuzzy.control.system.FuzzySystemSetting;
import hr.fer.mekrac.fuzzy.control.system.RudderFuzzySystemMin;

import java.util.Scanner;

/**
 * @author matejc
 * Created on 09.11.2022.
 */

public class FuzzyControlSystem {
    public static void main(String[] args) {

        IDefuzzifier defuzzifier = new COADefuzzifier();

        FuzzySystem fsAcceleration = new AccelerationFuzzySystemMin(defuzzifier, FuzzySystemSetting.MINIMUM);
        FuzzySystem fsRudder = new RudderFuzzySystemMin(defuzzifier, FuzzySystemSetting.MINIMUM);

        try (Scanner scanner = new Scanner(System.in).useDelimiter("\\n")) {
            while (scanner.hasNext()) {
                String line = scanner.next();
                if (line.equalsIgnoreCase("kraj")) break;


                CrispInputReading crispInputReading = parseInputString(line);

                int acceleration = fsAcceleration.decide(crispInputReading);
                int rudder = fsRudder.decide(crispInputReading);

                System.out.printf("%d %d%n", acceleration, rudder);
//                System.err.printf("%s%n%d %d%n", crispInputReading, acceleration, rudder);
                System.out.flush();
            }
        }
    }

    public static CrispInputReading parseInputString(String line) {
        var split = line.split(" ");

        int left = Integer.parseInt(split[0]);
        int right = Integer.parseInt(split[1]);
        int leftAngle = Integer.parseInt(split[2]);
        int rightAngle = Integer.parseInt(split[3]);
        int speed = Integer.parseInt(split[4]);
        boolean aboutRight = split[5].equals("1");

        return new CrispInputReading(left, right, leftAngle, rightAngle, speed, aboutRight);
    }
}
