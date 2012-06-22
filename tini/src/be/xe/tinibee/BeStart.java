package be.xe.tinibee;

import com.dalsemi.system.*;
import com.dalsemi.system.I2CPort;

import java.util.Vector;

import be.xe.tinibee.*;


public class BeStart 
{
    public static void main(String[] args) 
    {
        String root_url = "46.19.33.55";
        if( args.length != 0)
            root_url = args[0];
        UDPPublisher pb = new UDPPublisher(root_url);	
        System.err.println("Publishing to "+root_url);
        /* Initialize the i2c bus */

        I2CPort i2c = new I2CPort();
        i2c.setClockDelay((byte)2);
        MaxADC adc1 = new MaxADC((byte)0x28,i2c);
        MaxADC adc2 = new MaxADC((byte)0x2F,i2c);
        Metric weight = new Metric("ohain.weight",4);
        double[] a = {0.049,0.039,0.039,0.049};
        double[] b = {-7.1 ,9.8  ,16.9 ,-3.6};
        LinearCal lc = new LinearCal(a,b);

        TempSensor sens = new TempSensor();
        Metric temperature = new Metric("ohain.temp",1);


        Vector data = new Vector();
        data.addElement(temperature);
        data.addElement(weight);
        System.out.println("Starting publisher");
        try {
            while( true )
            {               
                temperature.set(0,sens.getTemp());
                weight.set(0,adc2.getValue((byte)4));
                weight.set(1,adc2.getValue((byte)5));
                weight.set(2,adc2.getValue((byte)6));
                weight.set(3,adc2.getValue((byte)7));
//                weight.calibrate(lc);
                pb.post(data);
                Thread.sleep(4000);
            }
        }
        catch (InterruptedException dummy)
        {
            System.out.println("Interrupted exitting");
        }

    }
}
