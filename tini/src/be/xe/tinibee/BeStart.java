package be.xe.tinibee;


import java.util.Vector;

import be.xe.tinibee.*;


public class BeStart 
{
	public static void main(String[] args) 
    {
        String root_url = "46.19.33.55";
        if( args.length != 0)
            root_url = args[0];
        //HTTPPublisher pb = new HTTPPublisher(root_url);
        UDPPublisher pb = new UDPPublisher(root_url);	
        //Publisher pb = new Publisher("http://127.0.0.1:8880/publish");
        System.err.println("Publishing to "+root_url);
        TempSensor sens = new TempSensor();
        //	String[] names = {"det 1","det2","det3"};
        //	Double[] values = {1.0,2.0,3.0};

        Vector metrics = new Vector();
        Metric temperature = new Metric("cam.temp",1);
        metrics.addElement(temperature);
        System.out.println("Starting publisher");
        try {
            while( true )
            {               
                temperature.set(0,sens.getTemp());
               // values[0]=values[0]+1.0;
                pb.post(metrics);
                Thread.sleep(4000);
            }
        }
        catch (InterruptedException dummy)
        {
            System.out.println("Interrupted exitting");
        }

    }
}
