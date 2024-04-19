package SchoolSystem;

import java.util.HashMap;

public class School {
    private String name;
    private String location;
    private int totalStudents;
    private HashMap<String, Student> students = new HashMap<String, Student>();

    public School(String n, String l, int t) {
        name = n;
        location = l;
        totalStudents = t;
        students.clear();
    }

    public School() {
        name = "";
        location = "";
        totalStudents = 0;
        students.clear();
    }

    public String getName() {
        return name;
    }

    public String getLocation() {
        return location;
    }

    public int getTotalStudents() {
        return totalStudents;
    }

    public void setName(String n) {
        name = n;
    }

    public void setLocation(String l) {
        location = l;
    }

    public void setTotalStudents(int t) {
        totalStudents = t;
    }

    public void addStudent(Student s) {
        totalStudents++;
        students.put(s.getName(), s);
    }

    public void removeStudent(Student s) {
        totalStudents--;
        students.remove(s.getName());
    }

    public String toString() {
        String output = "School: " + name + "\nLocation: " + location + "\nStudents in School: " + totalStudents + "\nStudents:\n";
        for(String s : students.keySet()) {
            output +=  "  - " + s.toString() + '\n';
        }
        return output;
    }
}
