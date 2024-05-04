package P1_Grocery;

import java.util.*;

public class GroceryList {
    private ArrayList<String> list = new ArrayList<String>();

    // constructors
    public GroceryList(ArrayList<String> l) {
        list = l;
    }

    public GroceryList() {
        list.clear();
    }

    public void setGroceryList(ArrayList<String> l) {
        list = l;
    }

    public void addItem(String i) {
        list.add(i);
    }

    public ArrayList<String> getGroceryList() {
        return list;
    }

    public int getGroceryListSize() {
        return list.size();
    }

    public String getItem(int index) {
        return list.get(index);
    }
    
    // linear search
    public boolean hasItem(String item) {
        for(String i : list) {
            if(i.equals(item)) {
                return true;
            }
        }
        return false;
    }

    // swap function
    private void swap(int i, int j) {
        String temp = list.get(i);
        list.set(i, list.get(j));
        list.set(j, temp);
    }

    // quick sort
    private int partition(int low, int high) {
        String pivot = list.get(high);
        int i = low - 1;

        for (int j = low; j <= high - 1; j++) {
            if (list.get(j).compareTo(pivot) < 0) {
                swap(++i, j);
            }
        }
        swap(i + 1, high);
        return i + 1;
    }

    public void sortGroceryList(int low, int high) {
        if (low < high) {
            int pi = partition(low, high);
            sortGroceryList(low, pi - 1);
            sortGroceryList(pi + 1, high);
        }
    }

    public String toString() {
        return list.toString();
    }
}
