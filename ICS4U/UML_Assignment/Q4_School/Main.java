import SchoolSystem.*;

public class Main {
	public static void main(String[] args){
		School ldh = new School("Longfields", "Barrhaven", 2000); 
		Student aaron = new Student("Aaron", 12);
		Course math = new Course("Math", 30, "Ms. Hang", "Calculus & Vectors", 65);
		Course cs = new Course("Computer Science", 20, "Ms. Luce", "Course on Java/OOP", 85);
		Club codeClub = new Club("Code Club", 10, "Ms. Luce", "Teach coding to students");
		Award mathAward = new Award("Math Award", "Highest grade in Math Course", 100);

		ldh.addStudent(aaron);
		aaron.addCourse(math);
		aaron.addCourse(cs);
		aaron.joinClub(codeClub);
		aaron.achieveAward(mathAward);

		System.out.println(ldh);
		System.out.println("--------------------");
		System.out.println(aaron);
	}
}