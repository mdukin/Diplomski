package oer_lab1;

public class Clause {
	int[] indexes;
	public Clause(int[] indexes) {
		this.indexes = indexes;
	}
	// vraća broj literala koji čine klauzulu
	public int getSize() {
		return this.indexes.length;
	}
	// vraća indeks varijable koja je index-ti član ove klauzule
	public int getLiteral(int index) {
		return indexes[index];
	}
	// vraća true ako predana dodjela zadovoljava ovu klauzulu
	public boolean isSatisfied(BitVector assignment) {
		for(int i = 0; i < this.getSize(); i++) {
			int indexVarijable = this.getLiteral(i) ;
			boolean pozitivnaVarijabla = indexVarijable > 0 ? true : false;
			boolean bit = assignment.get(Math.abs(indexVarijable) - 1);
			if(pozitivnaVarijabla && bit ||
					!pozitivnaVarijabla && !bit ) return true;
		}
		return false;
	}
	@Override
	public String toString() {
		return "";
	}
}