package ShapeType;

import java.lang.Math;

public class Triangle extends Shape {
    private double side1 = 0;
    private double side2 = 0;
    private double side3 = 0;

    public Triangle(double s1, double s2, double s3) {
        side1 = s1;
        side2 = s2;
        side3 = s3;
    }

    public Triangle() {
        side1 = 0;
        side2 = 0;
        side3 = 0;
    }

    public double getSide1() {
        return side1;
    }

    public double getSide2() {
        return side2;
    }

    public double getSide3() {
        return side3;
    }

    public void setSide1(double s1) {
        side1 = s1;
    }

    public void setSide2(double s2) {
        side2 = s2;
    }

    public void setSide3(double s3) {
        side3 = s3;
    }

    public double getArea() {
        double semiPerimeter = (side1 + side2 + side3)/2.0;
        return Math.sqrt(semiPerimeter*(semiPerimeter-side1)*(semiPerimeter-side2)*(semiPerimeter-side3));
    }

    public double getPerimeter() {
        return side1 + side2 + side3;
    }
}