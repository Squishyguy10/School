package SchoolSystem;

public class Club {
    private String name;
    private int clubSize;
    private String supervisor;
    private String description;

    public Club(String n, int size, String s, String desc) {
        name = n;
        clubSize = size;
        supervisor = s;
        description = desc;
    }

    public Club() {
        name = "";
        clubSize = 0;
        supervisor = "";
        description = "";
    }

    public String getName() {
        return name;
    }

    public int getClubSize() {
        return clubSize;
    }

    public String getSupervisor() {
        return supervisor;
    }

    public String getDescription() {
        return description;
    }

    public void setName(String n) {
        name = n;
    }

    public void setClubSize(int size) {
        clubSize = size;
    }

    public void setSupervisor(String s) {
        supervisor = s;
    }

    public void setDescription(String desc) {
        description = desc;
    }

    public String toString() {
        return " - " + name + "\n    " + description + "\n    Club Size: " + clubSize + "\n    Teacher Supervisor: " + supervisor + '\n';
    }
}
