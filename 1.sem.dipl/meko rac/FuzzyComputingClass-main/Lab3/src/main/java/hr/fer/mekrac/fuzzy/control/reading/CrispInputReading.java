package hr.fer.mekrac.fuzzy.control.reading;

/**
 * @author matejc
 * Created on 09.11.2022.
 */

public record CrispInputReading(int left, int right, int leftAngle, int rightAngle, int speed, boolean rightPath) {
    public int[] getValuesAsArray() {
        return new int[]{left, right, leftAngle, rightAngle, speed, rightPath ? 1 : 0};
    }
}
