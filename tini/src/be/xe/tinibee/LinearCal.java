package be.xe.tinibee;

import be.xe.tinibee.*;


public class LinearCal implements Calibrator
{
    double[] a; 
    double[] b;

    LinearCal( double[] a, double[] b)
    {
        this.a = a; 
        this.b = b;
    }

    public double calibrate( int k,  double v)
    {
//        System.err.println(a[k]);
        return a[k]*v+b[k];
    }


}
