package ooup_lab3.plugins;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import ooup_lab3.ClipboardStack;
import ooup_lab3.Plugin;
import ooup_lab3.TextEditorModel;

public class VelikoSlovoPlugin implements Plugin{

	@Override
	public String getName() {
		// TODO Auto-generated method stub
		return "VelikoSlovo";
	}

	@Override
	public String getDescription() {
		// TODO Auto-generated method stub
		return "pretvara svaku riječ u veliko slovo";
	}

	@Override
	public void execute(TextEditorModel model, ClipboardStack clipboardStack) {
		List<String> newList = new ArrayList<>();
		Iterator<String> it = model.allLines();
		while(it.hasNext()) {
			String[] words = it.next().split(" ");
			if(words.length == 0) {
				newList.add(""); continue;
			}
			StringBuilder sb = new StringBuilder();
			for (String word : words) {
				if(word.length() > 0)
				 sb.append(Character.toUpperCase(word.charAt(0)))
                 .append(word.substring(1).toLowerCase())
                 .append(" ");
			}
			newList.add(sb.toString().trim());
		}
		model.setLines(newList);
		model.notifyTextObservers();
		
	}

}
