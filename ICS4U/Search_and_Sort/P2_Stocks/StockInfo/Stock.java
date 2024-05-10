package StockInfo;

public class Stock {
    private String name;
    private double price;

    public Stock(String n, double p) {
        name = n;
        price = roundPrice(p);
    }

    public Stock() {
        name = "";
        price = 0;
    }

    public void setName(String n) {
        name = n;
    }

    public void setPrice(double p) {
        price = roundPrice(p);
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    private double roundPrice(double p) {
        return Math.round(p * 100.0) / 100.0;
    }

    public String toString() {
        return name + ": $" + price + '\n';
    }
}
