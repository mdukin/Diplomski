package ooup_lab3;

import java.util.Stack;

public class UndoManager {
	
    public static UndoManager getInstance() {
		if(instance == null) {
			instance = new UndoManager();
		};
		return instance;
    }
	
    static UndoManager instance;
	Stack<EditAction> undoStack;
	Stack<EditAction> redoStack;
	//undo(); // skida naredbu s undoStacka, pusha je na redoStack i izvrsava
	//push(EditAction c); // brise redoStack, pusha naredbu na undoStack

}
