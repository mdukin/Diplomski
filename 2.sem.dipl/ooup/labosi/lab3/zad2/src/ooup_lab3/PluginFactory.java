package ooup_lab3;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;

public class PluginFactory {


    public static Plugin newInstance(String pluginName) 
    		throws ClassNotFoundException, IllegalAccessException, InstantiationException, NoSuchMethodException, InvocationTargetException {
    	
        Class<?> opisnik = Class.forName("ooup_lab3.plugins." +pluginName);
        
        Constructor<?> ctr = opisnik.getConstructor();

        return (Plugin)ctr.newInstance();
    }
}