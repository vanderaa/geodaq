package be.xe.tinibee;

import java.util.Vector;
import be.xe.tinibee.*;

public interface Publisher
{
//	public void post(String[] names, long time, double[] values);
	public boolean post(Vector metrics); 
//	public boolean post_with_ack(String[] names, long time, double[] values);
//	public boolean post_with_ack(String[] names, double[] values);
}
