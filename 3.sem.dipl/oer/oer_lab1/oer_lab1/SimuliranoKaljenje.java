package oer_lab1;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class SimuliranoKaljenje {
	
	static Random rand = new Random();
	static double alpha = 0.9;
	
	public static void main(String[] args) throws IOException {
		List<double[]> data = loadData("data/prijenosna.txt");
		double T = 1;
		
		double[] coefs = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0};
		
		for(int i = 0; i<10000; i++) {
			
			double[] neighbourCoefs = getNeighbour(coefs, T);
			double myErr = error(coefs, data);
			if(i %1000 == 0) System.out.println(myErr);
			double neighbourErr = error(neighbourCoefs, data);
			double deltaE = neighbourErr - myErr;
	        if (deltaE < 0 || rand.nextDouble() < Math.exp(-deltaE / T)) 
                coefs = neighbourCoefs; 
	        T *= alpha;
		}
		
	}
	
	private static double[] getNeighbour(double[] coefs, double T) {
        double[] neighbor = coefs.clone();
        
        for (int i = 0; i < neighbor.length; i++) {
            neighbor[i] += (rand.nextDouble(-1, 1)) ;
        }
        return neighbor;
	}

	public static List<double[]> loadData(String filePath) throws IOException{
		List<double[]> data = new ArrayList<>();
		Path p = Path.of(filePath);
		Scanner scan = new Scanner(p);
		while(scan.hasNextLine()) {
			String line = scan.nextLine();
            line = line.replace("[", "").replace("]", "").trim();
            String[] stringValues = line.split(",");
            double[] values = new double[stringValues.length];
            for (int i = 0; i < stringValues.length; i++) {
                values[i] = Double.parseDouble(stringValues[i].trim());
            }
            data.add(values);
		}
		return data;
	}
	
	public static double error(double[] coefs,List<double[]> data) {
		
		double err_sum = 0;
		for(double[] X : data) {
			double y_hat = coefs[0] * X[0] +
						   coefs[1] * Math.pow(X[0], 3)* X[1] +
			coefs[2]* Math.exp(coefs[3]*X[2])*(1+Math.cos(coefs[4]*X[3]))+
			coefs[5]*X[3]*Math.pow(X[4], 2);
			double y_real = X[5];
			err_sum += Math.abs(y_real-y_hat);
		}

		return err_sum / data.size();
	}

}
