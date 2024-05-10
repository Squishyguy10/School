import java.util.Scanner;

import StockInfo.*;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        Market market = new Market();

        while(true) {
            System.out.print("Enter a stock name (enter \"stop\" to quit): ");
            String name = input.next();
            if(name.equals("stop")) {
                break;
            }
            double price;
            while(true) {
                System.out.print("Enter a price for " + name + ": ");
                if(input.hasNextDouble()) {
                    price = input.nextDouble();
                    if(price > 0) {
                        break;
                    }
                    else {
                        System.out.println("Price must be greater than 0. Please try again.");
                    }
                }
                else {
                    System.out.println("Invalid input. Please enter a valid price.");
                    input.next();
                }
            }
            market.addStock(new Stock(name, price));
        }

        market.sortPrices();
        System.out.println("Sorted market:\n--------------------\n" + market);

        while(true) {
            System.out.print("Find a stock price (enter \"0\" to quit): ");
            double price = 0.0;
            while(true) {
                if(input.hasNextDouble()) {
                    price = Math.round(input.nextDouble() * 100.0) / 100.0;
                    if(price >= 0.0) {
                        break;
                    }
                    else {
                        System.out.println("Price must be greater than 0. Please try again.");
                    }
                }
                else {
                    System.out.println("Invalid input. Please enter a valid price.");
                    input.next();
                }
            }
            if(price == 0.0) {
                break;
            }
            int index = market.hasPrice(price);
            if(index == -1) {
                System.out.println("A stock with price $" + price + " was not found");
            }
            else {
                System.out.println(market.getStockName(index) + " has a price of $" + price);
            }
        }
    }
}