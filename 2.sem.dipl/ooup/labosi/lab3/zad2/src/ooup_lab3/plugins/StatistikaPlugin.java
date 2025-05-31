package ooup_lab3.plugins;

import java.util.Iterator;

import javax.swing.JOptionPane;

import ooup_lab3.ClipboardStack;
import ooup_lab3.Plugin;
import ooup_lab3.TextEditorModel;

public class StatistikaPlugin implements Plugin {
	
	public StatistikaPlugin() {
		System.out.println("im here");
	}
    @Override
    public String getName() {
        return "Statistika";
    }

    @Override
    public String getDescription() {
        return "Broji redove, rijeci i slova u dokumentu.";
    }

    @Override
    public void execute(TextEditorModel model, ClipboardStack clipboardStack) {
        int lineCount = 0;
        int wordCount = 0;
        int charCount = 0;

        Iterator<String> it = model.allLines();
        while (it.hasNext()) {
            String line = it.next();
            lineCount++;
            String[] words = line.split("\\s+");
            wordCount += words.length;
            charCount += line.replaceAll("\\s+", "").length();
        }
    	String message = String.format("Statistics:\nLines: %d\nWords: %d\nCharacters (excluding spaces): %d",
                lineCount, wordCount, charCount);
        JOptionPane.showMessageDialog(null, message, "Document Statistics", JOptionPane.INFORMATION_MESSAGE);

    }


}