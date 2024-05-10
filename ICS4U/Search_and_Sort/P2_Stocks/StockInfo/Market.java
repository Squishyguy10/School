package StockInfo;

import java.util.*;

public class Market {
    private ArrayList<Stock> stocks = new ArrayList<Stock>();

    // constructors
    public Market(ArrayList<Stock> s) {
        stocks = s;
    }

    public Market() {
        stocks.clear();
    }

    public void setStocks(ArrayList<Stock> s) {
        stocks = s;
    }

    public void addStock(Stock s) {
        stocks.add(s);
    }

    public ArrayList<Stock> getStocks() {
        return stocks;
    }

    public int getStocksSize() {
        return stocks.size();
    }

    public Stock getStock(int index) {
        return stocks.get(index);
    }

    public double getStockPrice(int index) {
        return stocks.get(index).getPrice();
    }

    public String getStockName(int index) {
        return stocks.get(index).getName();
    }

    // binary search
    public int hasPrice(double p) {
        int low = 0;
        int high = stocks.size()-1;
        while(low <= high) {
            int mid = low + (high-low)/2;
            if(getStockPrice(mid) == p) {
                return mid;
            }

            if(getStockPrice(mid) < p) {
                low = mid+1;
            }
            else {
                high = mid-1;
            }
        }
        // if not found
        return -1;
    }

    public void sortPrices() {
        for(int i = 0; i < stocks.size() - 1; i++) {
            boolean swapped = false;
            for(int j = 0; j < stocks.size() - i - 1; j++) {
                if(getStockPrice(j) > getStockPrice(j+1)) {
                    Stock temp = getStock(j);
                    stocks.set(j, getStock(j+1));
                    stocks.set(j+1, temp);
                    swapped = true;
                }
            }
            if(!swapped) {
                break;
            }
        }
    }

    public String toString() {
        String output = "";
        for(Stock s : stocks) {
            output += s;
        }
        return output;
    }
}
