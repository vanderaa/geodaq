package be.xe.tinibee;

import java.io.*;
import com.dalsemi.onewire.adapter.*;
import com.dalsemi.onewire.container.*;
import com.dalsemi.onewire.OneWireException;
import be.xe.tinibee.*;


public class CounterSensor
{
  int   count; 
  
  TINIExternalAdapter adapter =  null ;
  OneWireContainer1D sensor = null; 
  
  public CounterSensor()
  {
      try 
      {
          adapter = new TINIExternalAdapter();
          adapter.targetFamily(0x1D);
          sensor = (OneWireContainer1D)adapter.getFirstDeviceContainer();
      } 
      catch (OneWireException ex)
      {
          System.out.println("Oops could not create adapter");
      }
  }
  /** Return the current temperature
   */
  public double[] getCount()
  {
    double[] data = new double[2];

    try 
    {

        if( sensor != null && sensor.isPresent() )
        {
            data[0]=sensor.readCounter(0);
            data[1]=sensor.readCounter(1);
            return data;
        }
    } 
    catch (OneWireException ex)
    {
        System.out.println("Could not speak with device");
    }
    return null; 
  }

}
