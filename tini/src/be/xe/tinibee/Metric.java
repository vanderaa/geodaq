package be.xe.tinibee;


import be.xe.tinibee.*;

public class Metric 
{
    String   name; 
    double[] vals;

    Metric( String name, int len )
    {
        this.name = name;
        this.vals = new double[len]; 
    }
    void set( int i, double v )
    {
        vals[i] = v; 
    }
    double get( int i )
    {
        return vals[i];
    } 
    String name()
    {
        return name;
    }
    double[] get()
    {
        return vals;
    }
    int size()
    {
        return this.vals.length;
    }
    void calibrate(Calibrator c)
    {
        for( int k=0; k < vals.length; k++ )
        {
            vals[k] = c.calibrate(k,vals[k]);
        }

    }
}
