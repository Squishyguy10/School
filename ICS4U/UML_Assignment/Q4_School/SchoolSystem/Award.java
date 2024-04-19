package SchoolSystem;

public class Award {
    private String name;
    private String description;
    private int dollarAmount;

    public Award(String n, String desc, int amount) {
        name = n;
        description = desc;
        dollarAmount = amount;
    }

    public Award() {
        name = "";
        description = "";
        dollarAmount = 0;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public int getDollarAmount() {
        return dollarAmount;
    }

    public void setName(String n) {
        name = n;
    }

    public void setDescription(String desc) {
        description = desc;
    }

    public void setDollarAmount(int amount) {
        dollarAmount = amount;
    }

    public String toString() {
        return " - " + name + "\n    " + description + "\n    Cash Reward: " + dollarAmount + '\n';
    }
}