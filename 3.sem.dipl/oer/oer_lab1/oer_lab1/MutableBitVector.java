package oer_lab1;

import java.util.List;

public class MutableBitVector extends BitVector {
	public MutableBitVector(boolean... bits) {
		super(bits);	
	}
	public MutableBitVector(int n) {
		super(n);
	}
	
	// zapisuje predanu vrijednost u zadanu varijablu
	public void set(int index, boolean value) {
		bitsList.set(index, value);
	}

}
