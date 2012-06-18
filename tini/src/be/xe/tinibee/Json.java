package be.xe.tinibee;

import java.util.Vector;
import be.xe.tinibee.*;

public class Json
{

    public static String dumps( Metric metric )
    {
        double[] vals = metric.get();
        String retval = "\""+metric.name()+"\":[";
        for( int i=0; i < vals.length; i++) 
        {
            retval = retval + Double.toString(vals[i]);
            if( i < metric.size()-1 )
                retval = retval + ",";
        }
        retval = retval+ "]";
        return retval;
    }


    public static String dumps( Vector metrics )
    {
        String retval = "{";
        Metric m;
        for( int i=0; i < metrics.size(); i++ )
        {
            m = (Metric)metrics.elementAt(i); 
            retval = retval + Json.dumps(m);    
            if( i < metrics.size()-1 )
                retval = retval + ","; 
        }
        retval = retval + "}";
        return retval;

    }




}
