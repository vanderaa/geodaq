package be.xe.tinibee;

import be.xe.tinibee.*;


public class BeStart 
{
	public static void main(String[] args) 
    {
        String root_url = "192.168.1.35";
        if( args.length != 0)
            root_url = args[0];
        //HTTPPublisher pb = new HTTPPublisher(root_url);
        UDPPublisher pb = new UDPPublisher(root_url);	
        //Publisher pb = new Publisher("http://127.0.0.1:8880/publish");
        System.err.println("Publishing to "+root_url);
        TempSensor sens = new TempSensor();
        //	String[] names = {"det 1","det2","det3"};
        //	Double[] values = {1.0,2.0,3.0};
        String[] names = {"TempCambridge"};
        double[] values = new double[1];
        values[0]=0;
        System.out.println("Starting publisher");
        try {
            while( true )
            {               

               	values[0]=sens.getTemp();
               // values[0]=values[0]+1.0;
                pb.post(names, values);
                Thread.sleep(4000);
            }
        }
        catch (InterruptedException dummy)
        {
            System.out.println("Interrupted exitting");
        }

    }
}
