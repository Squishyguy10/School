package SchoolSystem;

public class Course extends Club {
    private int mark;

    public Course(String name, int size, String teacher, String desc, int m) {
        super(name, size, teacher, desc);
        mark = m;
    }
    
    public Course() {
        super("", 0, "", "");
        mark = 0;
    }

    public int getClassSize() {
        return super.getClubSize();
    }

    public String getTeacher() {
        return super.getSupervisor();
    }

    public int getMark() {
        return mark;
    }

    public void setClassSize(int size) {
        super.setClubSize(size);
    }

    public void setTeacher(String t) {
        super.setSupervisor(t);
    }

    public void setMark(int m) {
        mark = m;
    }

    public char getMarkLevel() {
        if(mark >= 80) {
            return '4';
        }
        if(mark >= 70) {
            return '3';
        }
        if(mark >= 60) {
            return '2';
        }
        if(mark >= 50) {
            return '1';
        }
        return 'R';
    }

    public String toString() {
        return " - " + super.getName() + "\n    " + super.getDescription() + "\n    Class Size: " + getClassSize() + "\n    Teacher: " + getTeacher() + "\n    Mark: " + mark + "\n    Mark Level: " + getMarkLevel() + '\n';
    }
}
