package ShapeType;

public class Square extends Rectangle {
    public Square(double s) {
        super(s, s);
    }

    public Square() {
        super(0, 0);
    }

    public double getSideLength() {
        return super.getLength();
    }

    public void setSideLength(double s) {
        super.setLength(s);
        super.setWidth(s);
    }
}