package ShapeType;

public abstract class Shape {
    public abstract double getArea();

    public abstract double getPerimeter();

    public String toString() {
        return getClass().getSimpleName() + ":\n" + String.format("Area: %.1f\nPerimeter: %.1f\n", getArea(), getPerimeter());
    }
}