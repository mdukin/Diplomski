package oer_lab1;

	public class SATFormula {
		
	int numberOfVariables; 
	Clause[] clauses;
	
	public SATFormula(int numberOfVariables, Clause[] clauses) {
		this.clauses = clauses;
		this.numberOfVariables = numberOfVariables;
	}
	public int getNumberOfVariables() {
		return this.numberOfVariables;
	}
	public int getNumberOfClauses() {
		return this.clauses.length;
	}
	public Clause getClause(int index) {
		return this.clauses[index];
	}
	public boolean isSatisfied(BitVector assignment) {
		for(Clause clause : clauses) {
			if(clause.isSatisfied(assignment)) continue;
			return false;
		}
		return true;
	}
	@Override
	public String toString() {
		return "";
	}
}