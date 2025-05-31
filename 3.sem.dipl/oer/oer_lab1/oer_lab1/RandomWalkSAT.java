package oer_lab1;

import java.util.Optional;
import java.util.Random;

public class RandomWalkSAT implements IOptAlgorithm{

    private SATFormula formula;
    private int maxTries=10000;
    private double p; 
    Random rand = new Random();

    public RandomWalkSAT(SATFormula formula, double p) {
        this.formula = formula;
        this.p = p;
    }
    
	@Override
	public Optional<BitVector> solve(BitVector initial) {
		MutableBitVector solution= initial.copy();
		for(int i = 0; i < maxTries; i++) {

			if(formula.isSatisfied(solution)) 
				return Optional.of(solution);
			
			Clause clause = formula.getClause(rand.nextInt(formula.getNumberOfClauses()));
			while(clause.isSatisfied(solution))
				 clause = formula.getClause(rand.nextInt(formula.getNumberOfClauses()));
			if(p >= rand.nextDouble()) {
				int var = clause.getLiteral(rand.nextInt(clause.getSize()));
				int index_var = Math.abs(var)-1;
				solution.set(index_var, !solution.get(index_var));
			}
			solution = getNextRandom(solution);
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
	
	public MutableBitVector getNextRandom(MutableBitVector solution) {
		MutableBitVector best = null;
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
		if(1-p >= rand.nextDouble())
			return best;
		else return solution;
	}

}
