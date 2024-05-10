package P1_Grocery;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        GroceryList list = new GroceryList(new ArrayList<String>(Arrays.asList("blueberry", "orange", "carrot", "apple", "grape")));
        
        while(true) {
            System.out.print("Check if an item is in the grocery list (enter \"quit\" to stop): ");
            String item = input.next();
            if(item.equals("quit")) {
                break;
            }
            if(list.hasItem(item)) {
                System.out.println(item + " was found in the list.");
            }
            else {
                System.out.print(item + " was not found in the list. Would you like to add it (Y/N): ");

                String ans = input.next().toUpperCase();
                while(!ans.equals("Y") && !ans.equals("N")) {
                    System.out.println("Invalid input. Would you like to add it (Y/N): ");
                    ans = input.next().toUpperCase();
                }
                if(ans.equals("Y")) {
                    System.out.println(item + " has been added to the list");
                    list.addItem(item);
                }
            }
        }
        list.sortGroceryList(0, list.getGroceryListSize()-1);
        System.out.println("Sorted Grocery List:\n" + list);
    }
}