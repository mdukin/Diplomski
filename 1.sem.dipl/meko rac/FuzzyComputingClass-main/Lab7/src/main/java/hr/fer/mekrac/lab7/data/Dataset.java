package hr.fer.mekrac.lab7.data;

import lombok.Getter;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

/**
 * @author matejc
 * Created on 13.01.2023.
 */

@Getter
public class Dataset {

    private final List<double[]> inputs;
    private final List<int[]> outputs;

    private Dataset(List<double[]> inputs, List<int[]> outputs) {
        this.inputs = inputs;
        this.outputs = outputs;
    }

    public int size() {
        return inputs.size();
    }

    public double[] getInputsAtIndex(int index) {
        return inputs.get(index);
    }

    public int[] getOutputsAtIndex(int index) {
        return outputs.get(index);
    }

    public static Dataset read(Path datasetPath) throws IOException {
        List<double[]> inputs = new ArrayList<>();
        List<int[]> outputs = new ArrayList<>();

        try (var reader = Files.newBufferedReader(datasetPath)) {
            String line = reader.readLine();

            while (line != null && !line.isEmpty()) {
                String[] split = line.split("\t");

                double[] input = {Double.parseDouble(split[0]), Double.parseDouble(split[1])};
                int[] output = {Integer.parseInt(split[2]), Integer.parseInt(split[3]), Integer.parseInt(split[4])};

                inputs.add(input);
                outputs.add(output);

                line = reader.readLine();
            }
        }

        return new Dataset(inputs, outputs);
    }
}
