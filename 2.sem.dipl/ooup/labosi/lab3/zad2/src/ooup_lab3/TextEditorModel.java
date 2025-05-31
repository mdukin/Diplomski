package ooup_lab3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

public class TextEditorModel {
	
	List<String> lines;
	LocationRange selectionRange = null;
	Location cursorLocation;
	List<CursorObserver> cursorObservers;
	List<TextObserver> textObservers;
	
	public TextEditorModel(String s) {
		String[] arr = s.split("\n");
		this.lines = new ArrayList<>(Arrays.asList(arr));
		this.cursorObservers = new ArrayList<>();
		this.cursorLocation = new Location(0, 0);
		this.textObservers = new ArrayList<>();
	}
	
	public void setLines(List<String> lines) {
		this.lines = lines;
	}
	public Iterator<String> allLines() {
		
		return linesRange(0, lines.size());
	}
	
	public Iterator<String> linesRange(int index1, int index2) {
		return new Iterator<String>() {
			
			private int currentIndex = index1;
			
			@Override	
			public boolean hasNext() {
                return currentIndex < index2 && currentIndex < lines.size();
			}

			@Override
			public String next() {
				if (hasNext()) return lines.get(currentIndex++);
				else throw new NoSuchElementException();
			}
		};
	}

	public void addCursorObserver(CursorObserver obs) {
		cursorObservers.add(obs);
	}
	public void removeCursorObserver(CursorObserver obs) {
		cursorObservers.remove(obs);
	}
	
	 public void notifyCursorObservers() {
	        for (CursorObserver observer : cursorObservers) {
	            observer.updateCursorLocation(cursorLocation);
	        }
	    }

	    public void moveCursorLeft() {
	        if (cursorLocation.x > 0) {
	        	cursorLocation.x--;
	        	notifyCursorObservers();
	        }
	    }

	    public void moveCursorRight() {
	    		if(cursorLocation.x <lines.get(cursorLocation.y).length()) {
		        	cursorLocation.x++;
	    		}
	        	notifyCursorObservers();

	    }

	    public void moveCursorUp() {
	        if (cursorLocation.y > 0) {
	        	cursorLocation.y--;
	        	if(cursorLocation.x > lines.get(cursorLocation.y).length())
	        		cursorLocation.x = lines.get(cursorLocation.y).length();
	        	notifyCursorObservers();
	        }
	    }

	    public void moveCursorDown() {
    		if(cursorLocation.y <lines.size() -1 ) {
	        	cursorLocation.y++;
	        	if(cursorLocation.x > lines.get(cursorLocation.y).length())
	        		cursorLocation.x = lines.get(cursorLocation.y).length();
	        	notifyCursorObservers();
    		}      
	    }
	    
	    
	    public void addTextObserver(TextObserver observer) {
	        textObservers.add(observer);
	    }

	    public void removeTextObserver(TextObserver observer) {
	        textObservers.remove(observer);
	    }

	    public void notifyTextObservers() {
			if(selectionRange != null) {
				 selectionRange.second = cursorLocation;
			}
	        for (TextObserver observer : textObservers) {
	            observer.updateText();
	        }
	    }
	    
	    public void deleteBefore() {
	    	System.out.println(selectionRange);
	        if (cursorLocation.x > 0) {
	            String text = lines.get(cursorLocation.y).substring(0, cursorLocation.x - 1) + lines.get(cursorLocation.y).substring(cursorLocation.x);
	            cursorLocation.x--;
	            lines.set(cursorLocation.y, text);
	        }
	        else if(cursorLocation.y > 0 && lines.get(cursorLocation.y).length()==0) {
	        	lines.remove(cursorLocation.y);
	        	cursorLocation.y--;
	        	cursorLocation.x = lines.get(cursorLocation.y).length();
	        }
	        	
	        notifyTextObservers();
	    }

	    public void deleteAfter() {
	        if (cursorLocation.x < lines.get(cursorLocation.y).length()) {
	            String text = lines.get(cursorLocation.y).substring(0, cursorLocation.x) + lines.get(cursorLocation.y).substring(cursorLocation.x + 1);
	            lines.set(cursorLocation.y, text);
	            notifyTextObservers();
	        }
	    }

	    public void deleteRange(LocationRange range) {
	    	List<String> newList = new ArrayList<String>();
	    	for(int i = 0; i < lines.size(); i++) {
	    		if(i == range.first.y && i == range.second.y) {
	    			newList.add(lines.get(i).substring(range.first.x, range.second.x));
	    		}
	    		else if(i == range.first.y) {
	    			newList.add(lines.get(i).substring(0,range.first.x));
	    		}
	    		else if(i == range.second.y) {
	    			newList.add(lines.get(i).substring(range.second.x));
	    		}
	    		else if(i < range.first.y || i > range.second.y)
	    			newList.add(lines.get(i));
	    	}
	    	setLines(newList);
	    	cursorLocation = new Location(0, 0);
	    	range = null;
	    	notifyCursorObservers();
	        notifyTextObservers();
	    }

	    public LocationRange getSelectionRange() {
	        return selectionRange;
	    }

	    public void setSelectionRange(LocationRange range) {
	        this.selectionRange = range;
	        notifyTextObservers();
	    }

	    
	    public void insert(char c) {
	    	String text =  lines.get(cursorLocation.y).substring(0, cursorLocation.x) + c + lines.get(cursorLocation.y).substring(cursorLocation.x);
            cursorLocation.x++;
            lines.set(cursorLocation.y, text);
            notifyTextObservers();
	    }
	    
	    public void insert(String str) {
	    	String text =  lines.get(cursorLocation.y).substring(0, cursorLocation.x) + str + lines.get(cursorLocation.y).substring(cursorLocation.x);
            cursorLocation.x += str.length();
            lines.set(cursorLocation.y, text);
            notifyTextObservers();
	    }

		public void enter() {
			String text1 =  lines.get(cursorLocation.y).substring(0, cursorLocation.x);
			String text2 = lines.get(cursorLocation.y).substring(cursorLocation.x);
			System.out.println(text2);
			if(text2== null) text2 = "";
			cursorLocation.x = text2.length();
			lines.set(cursorLocation.y++, text1);
			lines.add(cursorLocation.y, text2);

			notifyTextObservers();
			
		}

		public void shiftDown() {
			if(selectionRange == null) {
				 setSelectionRange(new LocationRange(cursorLocation));
			}
			else {
				notifyTextObservers();
			}
		}

		public void shiftUp() {
			selectionRange = null;
			
		}
		
		public String getTextFromRange() {
			StringBuilder sb = new StringBuilder();
        	for(int i= selectionRange.first.y; i<= selectionRange.second.y ;i++) {        
        		int xStart = selectionRange.first.y == i ? selectionRange.first.x : 0 ;
        		int xEnd =  selectionRange.second.y == i ?  selectionRange.second.x : lines.get(i).length();
        		sb.append(lines.get(i).substring(xStart, xEnd));
        		if(i != selectionRange.second.y) sb.append(" ");
        	}

        	return sb.toString();

		}
    
	
}
