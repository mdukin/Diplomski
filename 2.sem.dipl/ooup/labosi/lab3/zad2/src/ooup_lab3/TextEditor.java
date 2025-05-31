package ooup_lab3;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.File;
import java.nio.file.Paths;
import java.util.Iterator;
import java.util.List;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JToolBar;

public class TextEditor extends JFrame {

	private static final long serialVersionUID = 1L;
	
		TextEditorModel model;
		TextArea textArea ;
		ClipboardStack clipStack = new ClipboardStack();
		private JLabel statusLabel;
	 	private JMenuItem undoMenuItem;
	 	private JMenuItem redoMenuItem;
	 	private JMenuItem cutMenuItem;
	  	private JMenuItem copyMenuItem;
	    private JMenuItem pasteMenuItem;

	    private JButton undoButton;
	    private JButton redoButton;
	    private JButton cutButton;
	    private JButton copyButton;
	    private JButton pasteButton;

	    
        JMenuBar menuBar = new JMenuBar();

	
	public TextEditor(TextEditorModel model) {
		
		this.model = model;
		setSize(400, 400);
		setDefaultCloseOperation(DISPOSE_ON_CLOSE);
		setVisible(true);
		initGUI();
	}
	
	private void initGUI(){

		Container cp = getContentPane();
		cp.setLayout(new BorderLayout());
		
		textArea = new TextArea(model);
		
		statusLabel = new JLabel("cursor: " + model.cursorLocation.toString() + "  | lines: " + model.lines.size()) ;
		statusLabel.setBorder(BorderFactory.createLineBorder(getForeground(), 2));

		model.addCursorObserver(loc -> statusLabel.setText("cursor: " + loc.toString() + "  | lines: " + model.lines.size()));
		model.addTextObserver(()-> statusLabel.setText("cursor: " + model.cursorLocation.toString() + "  | lines: " + model.lines.size()));
		
		model.addCursorObserver((l)-> textArea.repaint() );
		model.addTextObserver(()-> textArea.repaint() );
		
		cp.add(textArea, BorderLayout.CENTER);
		cp.add(statusLabel, BorderLayout.SOUTH);
		
		addKeyListener(new MyListener() );
			
		createMenuBar();
		loadPlugins();
		createToolBar();
		

	}
	
	private class MyListener implements KeyListener{

		@Override
		 public void keyPressed(KeyEvent e) {
			
			if(e.isShiftDown()) {
				model.shiftDown();
			}
	        int keyCode = e.getKeyCode();
	        
	        if(e.isControlDown()) {
	        	switch (keyCode) {
	               case KeyEvent.VK_C:
	            	   clipStack.push(model.getTextFromRange());
	                   break;
	               case KeyEvent.VK_X:
	            	   clipStack.push(model.getTextFromRange());
	            	   model.deleteRange(model.getSelectionRange());;
	                   break;
	               case KeyEvent.VK_V:
	            	   model.insert(clipStack.peek());
	            	   if(e.isShiftDown())
	            		   clipStack.pop();
	                   break;
	        	}
	        
	        }
           switch (keyCode) {
               case KeyEvent.VK_LEFT:
                   model.moveCursorLeft();
                   break;
               case KeyEvent.VK_RIGHT:
                   model.moveCursorRight();
                   break;
               case KeyEvent.VK_UP:
                   model.moveCursorUp();
                   break;
               case KeyEvent.VK_DOWN:
                   model.moveCursorDown();
                   break;
               case KeyEvent.VK_BACK_SPACE:
                   if (model.getSelectionRange() == null) 
                       model.deleteBefore();
                   else 
                       model.deleteRange(model.getSelectionRange());
                   break;
               case KeyEvent.VK_DELETE:
                   if (model.getSelectionRange() == null) 
                       model.deleteAfter(); 
                   else 
                       model.deleteRange(model.getSelectionRange());
                   break;
               case KeyEvent.VK_ENTER:
                   model.enter();
                   break;
                   
               default:
                   if (!Character.isISOControl(e.getKeyChar()) && e.getKeyCode() != KeyEvent.VK_SHIFT  && e.getKeyCode() != KeyEvent.VK_CONTROL) {
                       model.insert(e.getKeyChar());
                       if(!e.isShiftDown())
                    	   model.shiftUp();        			
                   }
                   break;
           }
           
	        
		}

		@Override
		public void keyTyped(KeyEvent e) {
		}

		@Override
		public void keyReleased(KeyEvent e) {
		}
	};

		
	
	class TextArea extends JComponent{
		private static final long serialVersionUID = 1L;
		
        private TextEditorModel model;

        public TextArea(TextEditorModel model) {
            this.model = model;
        }
				
		@Override
		protected void paintComponent(Graphics g) {
			
			Iterator<String> it = model.allLines();
			Location cursorLocation = model.cursorLocation;
			
			Color selectionColor = Color.LIGHT_GRAY;
			Insets ins = getInsets();
			int x0 = ins.left;
			int y0 = ins.top;
			
			Font originalFont = g.getFont();
			g.setFont(originalFont.deriveFont(20f));
			
			FontMetrics fm = g.getFontMetrics();
			int lineHeight =  fm.getHeight();

                LocationRange selectionRange = model.getSelectionRange();
                if(selectionRange != null) {
                	g.setColor(selectionColor);               	
                	for(int i= selectionRange.first.y; i<= selectionRange.second.y ;i++) {                		
                		int y = (i+1) * lineHeight;
                		
                		int xStart = selectionRange.first.y != i ? 0 : fm.stringWidth(model.lines.get(i).substring(0, selectionRange.getFirst().x));
                		int xEnd =  selectionRange.second.y != i ?  fm.stringWidth(model.lines.get(i)) : fm.stringWidth(model.lines.get(i).substring(0, selectionRange.getSecond().x));
                		g.fillRect(xStart, y - lineHeight, xEnd - xStart, lineHeight);
                	}
                }  
            	g.setColor(Color.black);
    			while(it.hasNext()) {
    				g.drawString(
    						 it.next(),
    						 x0,y0 + fm.getAscent()
    						 );
    				y0 += lineHeight ;

    			}
    			
                int cursorX = x0 + fm.stringWidth(model.lines.get(cursorLocation.y).substring(0, cursorLocation.x));
                int cursorY = cursorLocation.y * lineHeight + ins.top;
                int cursorHeight = lineHeight ; 
                g.drawLine(cursorX, cursorY, cursorX, cursorY + cursorHeight); 
		}
	}


    private void loadPlugins() {
        JMenu menu = new JMenu("Plugins");
        menuBar.add(menu);
        
        String pluginDir = Paths.get(System.getProperty("user.dir"), "bin/ooup_lab3/plugins").toString();
        final File dir = new File(pluginDir);
        try {
        	
            for (final File fileEntry : dir.listFiles()) {
                if (!fileEntry.getName().endsWith(".class")) continue;
                String pluginName = fileEntry.getName().replace(".class", "");

                try {

                    final Plugin plugin;
                    plugin = PluginFactory.newInstance(pluginName);
                    

                    JMenuItem item = new JMenuItem(plugin.getName());
                    menu.add(item);
                    item.addActionListener(new ActionListener() {
                        @Override
                        public void actionPerformed(ActionEvent actionEvent) {
                            plugin.execute(model,  clipStack);
                            
                        }
                    });
                } catch (Exception e) {
                	System.out.println(e);
                    System.out.println(String.format("Plugin \"%s\" couldn't be loaded", pluginName));
                }
            }
        } catch (Exception e) {
            System.out.println(String.format("Can't access plugin directory"));
        }
    }
	
	 private void createMenuBar() {
		 
	        JMenu fileMenu = new JMenu("File");
	        fileMenu.add(new JMenuItem("Open"));
	        fileMenu.add(new JMenuItem("Save"));
	        fileMenu.add(new JMenuItem("Exit"));

	        JMenu editMenu = new JMenu("Edit");
	        undoMenuItem = new JMenuItem("Undo");
	        redoMenuItem = new JMenuItem("Redo");
	        cutMenuItem = new JMenuItem("Cut");
	        copyMenuItem = new JMenuItem("Copy");
	        pasteMenuItem = new JMenuItem("Paste");
	        editMenu.add(undoMenuItem);
	        editMenu.add(redoMenuItem);
	        editMenu.add(cutMenuItem);
	        editMenu.add(copyMenuItem);
	        editMenu.add(pasteMenuItem);
	        editMenu.add(new JMenuItem("Paste and Take"));
	        editMenu.add(new JMenuItem("Delete selection"));
	        editMenu.add(new JMenuItem("Clear document"));

	        JMenu moveMenu = new JMenu("Move");
	        moveMenu.add(new JMenuItem("Cursor to document start"));
	        moveMenu.add(new JMenuItem("Cursor to document end"));
	        
	        menuBar.add(fileMenu);
	        menuBar.add(editMenu);
	        menuBar.add(moveMenu);

	        setJMenuBar(menuBar);
	    }

	    private void createToolBar() {
	        JToolBar toolBar = new JToolBar();

	        undoButton = new JButton("Undo");
	        redoButton = new JButton("Redo");
	        cutButton = new JButton("Cut");
	        copyButton = new JButton("Copy");
	        pasteButton = new JButton("Paste");

	        toolBar.add(undoButton);
	        toolBar.add(redoButton);
	        toolBar.add(cutButton);
	        toolBar.add(copyButton);
	        toolBar.add(pasteButton);

	        add(toolBar, "North");
	    }
}
