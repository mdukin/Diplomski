package ga.data;

/**
 * @author matejc
 * Created on 14.11.2022.
 */

public record Reading (double x, double y, double fOut){
    public static Reading parseReading(String readingString) {
        String[] split = readingString.split("\t");
        return new Reading(Double.parseDouble(split[0]),
                Double.parseDouble(split[1]),
                Double.parseDouble(split[2]));
    }
}
