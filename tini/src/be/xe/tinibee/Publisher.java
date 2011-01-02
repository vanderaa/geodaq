package be.xe.tinibee;

import java.io.*; 
import java.net.*; 
import be.xe.tinibee.*;

public class Publisher
{
    String root = null;
    URL url = null;
    URLConnection connection = null;

    public Publisher(String location)
    {
        root = location;
    }    

    public void post(String[] names, double[] values)
    {
        try 
        {
            // Construct a Json type key value
            String data = "{";
            int len = Math.min(names.length, values.length);
            for( int i=0; i< len; i++)
            {
                data = data+"\""+names[i]+"\":"+Double.toString(values[i]);
                if(i < len - 1)
                    data = data + ",";
            }
            data = data + "}";
            System.err.print("Updating with "+data);
            data = URLEncoder.encode(data);
            //System.err.println(data);
            //url = new URL(root);
            url = new URL(root+"?data="+data);
            connection = url.openConnection();
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(
                        connection.getInputStream()));
            String inputLine;
            while ((inputLine = in.readLine()) != null) 
                System.err.println(" Status = "+inputLine);
            in.close(); 
            url = null;
            connection = null;
        } 
        catch (MalformedURLException e) 
        {
            System.err.println("Exception: " + e);
        }
        catch (IOException e) 
        {
            System.err.println("Exception: " + e);
        }
 
    } 

    public static void main(String[] args) 
    {
        String root_url = "http://192.168.1.35:8880/publish";
        if( args.length != 0)
            root_url = args[0];
        Publisher pb = new Publisher(root_url);	
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
