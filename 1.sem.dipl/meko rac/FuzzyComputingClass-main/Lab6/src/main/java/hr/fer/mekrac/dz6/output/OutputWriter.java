package hr.fer.mekrac.dz6.output;

import hr.fer.mekrac.dz6.Sample;

import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

/**
 * @author matejc
 * Created on 28.12.2022.
 */

public class OutputWriter {
    private OutputWriter() {
    }

    public static void writeSamplesToFile(String path, List<Sample> sampleList) {
        try (BufferedWriter writer = Files.newBufferedWriter(Path.of(path))) {
            for (Sample sample : sampleList) {
                String line = "%f %f %f%n".formatted(sample.x(), sample.y(), sample.z());
                writer.write(line);
            }
        } catch (IOException e) {
            System.err.println("Failed to write file.");
            System.err.println(e.getMessage());
        }
    }

    public static void writeArraysToFile(String path, List<double[]> values) {
        try (BufferedWriter writer = Files.newBufferedWriter(Path.of(path))) {
            for (double[] array : values) {
                StringBuilder sb = new StringBuilder();

                for (double value : array) {
                    sb.append(value);
                    sb.append(" ");
                }
                sb.append("\n");
                writer.write(sb.toString());

            }
        } catch (IOException e) {
            System.err.println("Failed to write file.");
            System.err.println(e.getMessage());
        }
    }
}
