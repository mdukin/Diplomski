package oer_lab1;

import java.util.Optional;
import java.util.Random;

public class GSAT implements IOptAlgorithm{
	
    private SATFormula formula;
    private int maxTries=10000;

    public GSAT(SATFormula formula) {
        this.formula = formula;
    }


	@Override
	public Optional<BitVector> solve(BitVector initial) {
		
		BitVector solution= initial;
		for(int i = 0; i < maxTries; i++) {
			if(formula.isSatisfied(solution)) {
				System.out.println(i);
				return Optional.of(solution);
			}
			solution =getNextBest(solution);
			if(solution == null) {System.out.println(i);break; }
		}
		return Optional.empty();
	}
	
	public int countWrongClauses(BitVector solution) {
		int countWrong = 0;
		for(Clause clause : formula.clauses) {
			if(!clause.isSatisfied(solution)) countWrong++;
		}
		return countWrong;
	}
	
	public BitVector getNextBest(BitVector solution) {
		BitVector best = null;
		int minWrong = countWrongClauses(solution);
		MutableBitVector other = solution.copy();
		for(int i = 0; i < solution.getSize();i++) {
			if(i!=0)
				other.set(i-1, solution.get(i-1));
			other.set(i, !solution.get(i));
			int otherCount = countWrongClauses(other);
			if(otherCount <= minWrong) {
				best = other.copy();
				minWrong = otherCount;
			}
				
		}
		return best;
	}

}
