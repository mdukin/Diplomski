package oer_lab1;

import java.util.Optional;
import java.util.Random;

public class TriSATSolver {
	
	public static void main(String...args) {
		 SATFormula formula = Utils.ReadFromFile("data/uf20-01.cnf");
		 BitVector initial = new BitVector(new Random(), formula.numberOfVariables);
		 IOptAlgorithm alg1 = new GSAT(formula);
		 IOptAlgorithm alg2 = new RandomWalkSAT(formula,0.5);
		 
		 Optional<BitVector> solution = alg1.solve(initial);
		 if(solution.isPresent()) {
			 BitVector sol = solution.get();
			 System.out.println("Imamo rješenje: " + sol);
		 } else {
		 System.out.println("Rješenje nije pronađeno.");
		 }
		 
		 solution = alg2.solve(initial);
		 if(solution.isPresent()) {
			 BitVector sol = solution.get();
			 System.out.println("Imamo rješenje: " + sol);
		 } else {
		 System.out.println("Rješenje nije pronađeno.");
		 }
		}

}
