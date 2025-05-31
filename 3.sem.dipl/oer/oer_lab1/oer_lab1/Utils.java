package oer_lab1;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Utils {

	public static SATFormula ReadFromFile(String fileName) {
		Path p = Path.of(fileName);
		Scanner scan;
		int numberOfVaiables=0; 
		int k = 0;
		Clause[] clauses = null; ;
		try {
			scan = new Scanner(p);
	        while (scan.hasNextLine()) {
	            String line = scan.nextLine();
	            if(line.charAt(0) == 'c') continue;
	            if(line.charAt(0) == '%') break;
	            if(line.charAt(0) == 'p') {
	            	String[] strArr = line.split(" ");
	            	numberOfVaiables = Integer.parseInt(strArr[2]);
	            	int numberOfClauses = Integer.parseInt(strArr[3]);
	            	clauses = new Clause[numberOfClauses];
	            	continue;
	            }
	            String[] strArr = line.split(" ");
	            int[] clauseArray = new int[strArr.length-1];
	            for(int i = 0; i < strArr.length-1; i++) {
	            	clauseArray[i] = Integer.parseInt(strArr[i]);
	            }
	            clauses[k++] = new Clause(clauseArray);
	            
	        }
	        scan.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return new SATFormula(numberOfVaiables, clauses);

	}

}
