package Election;

public class Candidate {
    private String name;
    private int id;
    private int votes = 0;

    // Constructors
    public Candidate(String n, int i) {
        name = n;
        id = i;
        votes = 0;
    }

    public Candidate() {
        name = "";
        id = 0;
        votes = 0;
    }

    // setters
    public void setName(String n) {
        name = n;
    }

    public void setId(int i) {
        id = i;
    }

    // getters
    public String getName() {
        return name;
    }

    public int getId() {
        return id;
    }

    public int getVotes() {
        return votes;
    }

    public void addVote() {
        votes++;
    }

    public String toString() {
        return id + ". " + name + "\n";
    }

    public String toStringWinner() {
        return "ID: " + id + ", Name: " + name + ", Votes: " + votes + "\n";
    }
}
