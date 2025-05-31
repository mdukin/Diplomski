package ooup_lab3;

import java.lang.reflect.InvocationTargetException;

import javax.swing.SwingUtilities;

public class Main {

	public static void main(String[] args) throws InvocationTargetException, InterruptedException {
		
		TextEditorModel model =
		new TextEditorModel("bla bla tekstsaad\n aasdad dorotej ad\n");
		
		TextEditor te = new TextEditor(model);
	}
}
	
