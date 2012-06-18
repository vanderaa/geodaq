package be.xe.tinibee;

import java.io.*; 
import java.net.*; 
import be.xe.tinibee.*;

public class HTTPPublisher 
{
    String root = null;
    URL url = null;
    URLConnection connection = null;

    public HTTPPublisher(String location)
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

    

}
