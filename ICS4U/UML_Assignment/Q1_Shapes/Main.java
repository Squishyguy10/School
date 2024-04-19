import ShapeType.*;

public class Main {
	public static void main(String[] args){
        Triangle myTriangle = new Triangle(3.0, 4.0, 5.0);
		Circle myCircle = new Circle(3.0);
		Hexagon myHexagon = new Hexagon(2.0);
		Rectangle myRectangle = new Rectangle(2.0, 3.0);
		Square mySquare = new Square(3.0);

		System.out.println(myTriangle);
		System.out.println(myCircle);
		System.out.println(myHexagon);
		System.out.println(myRectangle);
		System.out.println(mySquare);
	}
}