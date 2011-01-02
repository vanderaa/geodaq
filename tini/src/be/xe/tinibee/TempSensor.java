package be.xe.tinibee;

import java.io.*;
import com.dalsemi.onewire.adapter.*;
import com.dalsemi.onewire.container.*;
import com.dalsemi.onewire.OneWireException;
import be.xe.tinibee.*;


public class TempSensor
{
  int     currentTemperature;
  
  TINIExternalAdapter adapter =  null ;
  OneWireContainer10 sensor = null; 
  
  public TempSensor()
  {
      try 
      {
          adapter = new TINIExternalAdapter();
          adapter.targetFamily(0x10);
          sensor = (OneWireContainer10)adapter.getFirstDeviceContainer();
      } 
      catch (OneWireException ex)
      {
          System.out.println("Oops could not create adapter");
      }
  }
  /** Return the current temperature
   */
  public double getTemp()
  {
    byte[] state;

    try 
    {

        if( sensor != null && sensor.isPresent() )
        {
            state = sensor.readDevice(); 
            sensor.doTemperatureConvert(state);
            state = sensor.readDevice(); 
            return sensor.getTemperature(state);
        }
    } 
    catch (OneWireException ex)
    {
        System.out.println("Could not speak with device");
    }
    return Integer.MIN_VALUE; 
  }

}
