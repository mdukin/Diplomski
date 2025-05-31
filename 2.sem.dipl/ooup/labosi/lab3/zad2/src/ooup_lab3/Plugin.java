package ooup_lab3;

public interface Plugin {
    String getName();
    String getDescription();
    void execute(TextEditorModel model, ClipboardStack clipboardStack);
}