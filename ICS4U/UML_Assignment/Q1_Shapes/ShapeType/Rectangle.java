package ShapeType;

public class Rectangle extends Shape {
    private double length = 0;
    private double width = 0;

    public Rectangle(double l, double w) {
        length = l;
        width = w;
    }

    public Rectangle() {
        length = 0;
        width = 0;
    }

    public double getLength() {
        return length;
    }

    public double getWidth() {
        return width;
    }

    public void setLength(double l) {
        length = l;
    }

    public void setWidth(double w) {
        width = w;
    }

    public double getArea() {
        return length*width;
    }

    public double getPerimeter() {
        return 2.0*(length + width);
    }
}