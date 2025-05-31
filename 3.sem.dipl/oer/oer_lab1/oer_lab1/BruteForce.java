package oer_lab1;

import java.util.Optional;

public class BruteForce implements IOptAlgorithm{
	
	SATFormula formula;
	
	public BruteForce(SATFormula formula) {
		this.formula = formula;
	}
	@Override
	public Optional<BitVector> solve(BitVector initial) {
		BitVectorNGenerator gen = new BitVectorNGenerator(formula.getNumberOfVariables());
		for(BitVector n : gen) {
			if(formula.isSatisfied(n))
				System.out.println(n);
		}
		return Optional.empty();
	}

}
