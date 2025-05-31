package ooup_lab3;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class ClipboardStack {
	

	Stack<String> texts;
	List<ClipboardObserver> observers;
	
    public ClipboardStack() {
        texts = new Stack<>();
        observers = new ArrayList<>();
    }
    
    public void push(String text) {
        texts.push(text);
        notifyObservers();
    }
    
    public String pop() {
        if (!texts.isEmpty()) {
            notifyObservers();
            return texts.pop();
        }
        return null;
    }
    
    public String peek() {
        return texts.isEmpty() ? null : texts.peek();
    }

    public boolean isEmpty() {
        return texts.isEmpty();
    }

    public void clear() {
        texts.clear();
        notifyObservers();
    }
    
    public void addObserver(ClipboardObserver observer) {
        observers.add(observer);
    }

    public void removeObserver(ClipboardObserver observer) {
        observers.remove(observer);
    }

    private void notifyObservers() {
        for (ClipboardObserver observer : observers) {
            observer.updateClipboard();
        }
    }
}
