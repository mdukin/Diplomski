package hr.fer.mekrac.dz6.tasks;

import hr.fer.mekrac.dz6.SampleFactory;
import hr.fer.mekrac.dz6.output.OutputWriter;

/**
 * @author matejc
 * Created on 28.12.2022.
 */

public class Task3 {
    public static void main(String[] args) {
        OutputWriter.writeSamplesToFile("task3.txt", SampleFactory.sampleFunction(SampleFactory.LAB_FUNCTION, -4, 4, -4, 4));
    }
}
