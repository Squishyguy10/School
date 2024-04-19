package ShapeType;

public class Circle extends Shape {
    private double radius = 0;
    static final double PI = 3.14159265;

    public Circle(double r) {
        radius = r;
    }

    public Circle() {
        radius = 0;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double r) {
        radius = r;
    }

    public double getArea() {
        return PI*radius*radius;
    }

    public double getPerimeter() {
        return 2.0*PI*radius;
    }

    public String toString() {
        String output = getClass().getSimpleName() + ":\n" + String.format("Area: %.1f \nCircumference: %.1f\n", getArea(), getPerimeter());
        return output;
    }
}