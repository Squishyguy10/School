import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);

        SeriesCategory.printSeries();


        boolean flag = true;
        while(flag) {
            try {
                System.out.print("Input a series above: ");
                String seriesInput = input.next();
                SeriesCategory series = SeriesCategory.valueOf(seriesInput);
                flag = false;
                
                switch(series){
                    case ARITHMETIC:

                        break;
                    case GEOMETRIC:
                        break;
                    case FIBONACCI:
                        break;        
                    case FACTORIAL:
                        break;   
                }
            }
            catch(IllegalArgumentException e) {
                System.out.println("Invalid series");
                flag = true;
            }
        }
    }
}