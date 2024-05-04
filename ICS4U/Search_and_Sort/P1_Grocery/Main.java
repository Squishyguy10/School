package P1_Grocery;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        GroceryList list = new GroceryList(new ArrayList<String>(Arrays.asList("blueberry", "orange", "carrot", "apple", "grape")));
        
        String item = "";
        while(!item.equals("quit")) {
            System.out.print("Check if an item is in the grocery list (enter \"quit\" to stop): ");
            item = input.next();
            if(list.hasItem(item)) {
                System.out.println(item + "was found in the list.");
            }
            else {
                System.out.print(item + "was not found in the list. Would you like to add it (Y/N): ");
            }
        }
    }
}