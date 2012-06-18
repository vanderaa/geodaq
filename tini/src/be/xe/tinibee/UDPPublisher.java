package be.xe.tinibee;

import java.io.*; 
import java.net.*; 
import java.util.Vector;
import be.xe.tinibee.*;

public class UDPPublisher implements Publisher
{
    String root = null;
    DatagramSocket socket = null;
    InetAddress host = null;
    int port = 3001;

    public UDPPublisher(String host_name)
    {
        try 
        {
        socket =  new DatagramSocket();
        host = InetAddress.getByName(host_name);
        }
        catch (IOException e)
        {
            System.err.println("Exception: " + e);
        }
    }    

    public boolean post(Vector metrics)
    {
        try 
        {
            String str = Json.dumps(metrics);

            DatagramPacket sendPacket = new DatagramPacket(str.getBytes(), 
                                                           str.getBytes().length, 
                                                           host, port);
            socket.send(sendPacket);

            System.err.println(str);
            //url = new URL(root);

        } 
        catch (IOException e) 
        {
            System.err.println("Exception: " + e);
            return false;
        }
 
        return true;
    } 

    

}
