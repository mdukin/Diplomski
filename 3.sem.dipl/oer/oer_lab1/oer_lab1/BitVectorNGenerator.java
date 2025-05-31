package oer_lab1;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class BitVectorNGenerator implements Iterable<MutableBitVector> {
	
	int n;
	public BitVectorNGenerator(int n) {
		this.n = n;
	}
	// Vraća lijeni iterator koji na svaki next() računa sljedećeg susjeda
	@Override
	public Iterator<MutableBitVector> iterator() {
		return new Iterator<MutableBitVector>() {
			
			MutableBitVector bitVector = new MutableBitVector(n);
			int counter = 0;
			
			@Override
			public MutableBitVector next() {
	            if (!hasNext()) {
	                throw new NoSuchElementException();
	            }
	            for (int i = 0; i < n; i++) {
	                bitVector.set(i, (counter & (1 << i)) != 0);
	            }
				counter++;
				return bitVector;
			}
			
			@Override
			public boolean hasNext() {
				return counter < Math.pow(2, n);
			}
		};
	}
	// Vraća kompletno susjedstvo kao jedno polje
	public MutableBitVector[] createNeighborhood() {
		return null;
	}
}
