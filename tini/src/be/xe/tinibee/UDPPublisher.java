package be.xe.tinibee;

import java.io.*; 
import java.net.*; 
import be.xe.tinibee.*;

public class UDPPublisher implements Publisher
{
    String root = null;
  
    public UDPPublisher(String location)
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
			DatagramSocket clientSocket = new DatagramSocket();
			InetAddress IPAddress = InetAddress.getByName(root);
			byte[] sendData = new byte[1024];
            sendData = data.getBytes();
			DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, 9876);
			clientSocket.send(sendPacket);
			clientSocket.close();          
            
            //System.err.println(data);
            //url = new URL(root);
            
        } 
        catch (IOException e) 
        {
            System.err.println("Exception: " + e);
        }
 
    } 

    

}
