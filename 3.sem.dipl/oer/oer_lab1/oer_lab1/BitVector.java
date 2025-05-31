package oer_lab1;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class BitVector {
	
	List<Boolean> bitsList = new ArrayList<>();
	
	public BitVector(Random rand, int numberOfBits) {
		for(int i = 0; i < numberOfBits; i++) {
			bitsList.add(rand.nextFloat() >= 0.5 ? true : false);
		}
	}
	
	public BitVector(boolean ... bits) {
		for(boolean bit : bits)
			bitsList.add(bit);
	}
	public BitVector(int n) {
		for(int i = 0; i < n; i++)
			bitsList.add(false) ;
	}
	// vraća vrijednost index-te varijable
	public boolean get(int index) {
		return bitsList.get(index);
	}
	// vraća broj varijabli koje predstavlja
	public int getSize() {
		return bitsList.size();
	}
	@Override
	public String toString() {
	    StringBuilder sb = new StringBuilder();

	    for (boolean bit : bitsList) {
	        sb.append(bit ? '1' : '0');
	    }

	    return sb.toString();
	}
	// vraća promjenjivu kopiju trenutnog rješenja
	public MutableBitVector copy() {
		boolean[] arr = new boolean[this.getSize()];
		for(int i = 0; i < getSize(); i++)
			arr[i] = get(i);
		return new MutableBitVector(arr); 
	}
}
