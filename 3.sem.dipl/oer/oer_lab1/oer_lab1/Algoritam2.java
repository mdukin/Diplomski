package oer_lab1;

import java.util.Optional;
import java.util.Random;

public class Algoritam2 implements IOptAlgorithm{
	
	SATFormula formula;
	static int iter = 10000;
	public Algoritam2(SATFormula formula) {
		this.formula = formula;
	}

	@Override
	public Optional<BitVector> solve(BitVector initial) {
		
		BitVector solution = initial;
		
		for(int i = 0; i <iter; i++ ) {
			int reward = getReward(solution);
			
			solution =getBestNeighbour(solution, reward);
			if(solution == null) {System.out.println(i);break; }
			if(formula.isSatisfied(solution)) {
				System.out.println(i);
				return Optional.of(solution);
			}
		}
		return Optional.empty();
	}
	
	public int getReward(BitVector solution) {
		int reward = 0;
		for(Clause clause : formula.clauses) {
			if(clause.isSatisfied(solution)) reward++;
		}
		return reward;
	}
	
	public BitVector getBestNeighbour(BitVector solution,int reward) {
		BitVector best = null;
		int bestReward = reward;
		MutableBitVector other = solution.copy();
		for(int i = 0; i < solution.getSize();i++) {
			if(i!=0)
				other.set(i-1, solution.get(i-1));
			other.set(i, !solution.get(i));
			int otherReward = getReward(other);
			if(otherReward >= bestReward) {
				best = other.copy();
				bestReward = otherReward;
			}
				
		}
		return best;
	}

}
