package ShapeType;

import java.lang.Math; 

public class Hexagon extends Shape {
    private double sideLength = 0;

    public Hexagon(double s) {
        sideLength = s;
    }

    public Hexagon() {
        sideLength = 0;
    }

    public double getSideLength() {
        return sideLength;
    }

    public void setSideLength(double s) {
        sideLength = s;
    }

    public double getArea() {
        return 3.0*Math.sqrt(3.0)*sideLength*sideLength/2.0;
    }

    public double getPerimeter() {
        return 6.0*sideLength;
    }
}