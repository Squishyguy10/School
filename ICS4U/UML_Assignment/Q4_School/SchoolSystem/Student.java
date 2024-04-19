package SchoolSystem;

import java.util.ArrayList;

public class Student {
    private String name;
    private int grade;
    private ArrayList<Award> awards = new ArrayList<Award>();
    private ArrayList<Course> courses = new ArrayList<Course>();
    private ArrayList<Club> clubs = new ArrayList<Club>();

    public Student(String n, int g) {
        name = n;
        grade = g;
        awards.clear();
        courses.clear();
        clubs.clear();
    }

    public Student() {
        name = "";
        grade = 0;
        awards.clear();
        courses.clear();
        clubs.clear();
    }

    public String getName() {
        return name;
    }

    public int getGrade() {
        return grade;
    }

    public ArrayList<Award> getAwards() {
        return awards;
    }

    public ArrayList<Course> getCourses() {
        return courses;
    }

    public ArrayList<Club> getClubs() {
        return clubs;
    }

    public void setName(String n) {
        name = n;
    }

    public void setGrade(int g) {
        grade = g;
    }

    public void achieveAward(Award a) {
        awards.add(a);
    }

    public void addCourse(Course c) {
        courses.add(c);
    }

    public void joinClub(Club c) {
        clubs.add(c);
    }

    public String toString() {
        String output = "Name: " + name + "\nGrade: " + grade + "\nCourses:\n";
        for(Course c : courses) {
            output += c.toString() + '\n';
        }
        output += "Clubs:\n";
        for(Club c : clubs) {
            output += c.toString() + '\n';
        }
        output += "Awards:\n";
        for(Award a : awards) {
            output += a.toString() + '\n';
        }
        return output;
    }
}
