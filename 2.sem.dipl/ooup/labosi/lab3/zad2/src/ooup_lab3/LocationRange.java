package ooup_lab3;

public class LocationRange {
	
	Location first;
	Location second;
	
	public LocationRange(Location first, Location second) {
		this.first = first;
		this.second =second;
	}
	
	public LocationRange(Location l) {
		this.first = new Location(l.x,l.y);
		this.second =new Location(l.x,l.y);;
	}
	
	public Location getFirst() {
		return first;
	}
	public Location getSecond() {
		return second;
	}
	
	@Override
	public String toString() {
		return getFirst() + "," + getSecond();
	}

}
