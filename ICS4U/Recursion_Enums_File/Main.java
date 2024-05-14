import java.util.*;
import java.util.logging.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        ArrayList<String> output = new ArrayList<String>();

        SeriesCategory.printSeries();


        boolean flag = true;
        while(flag) {
            try {
                System.out.print("Input a series above: ");
                String seriesInput = input.next();
                SeriesCategory series = SeriesCategory.valueOf(seriesInput);
                flag = false;
                output.add(seriesInput);
                int sum = 0;
                
                switch(series){
                    case ARITHMETIC:
                        System.out.print("Starting int: ");
                        int startArith = input.nextInt();
                        output.add("Start: " + startArith);
                        System.out.print("Difference: ");
                        int diff = input.nextInt();
                        output.add("Difference: " + diff);
                        System.out.print("Number of terms: ");
                        int termsArith = input.nextInt();
                        output.add("Terms: " + termsArith);
                        sum = SeriesCategory.arithmeticSeries(startArith, diff, termsArith);
                        break;
                    case GEOMETRIC:
                        System.out.print("Starting int: ");
                        int startGeo = input.nextInt();
                        output.add("Start: " + startGeo);
                        System.out.print("Difference: ");
                        int ratio = input.nextInt();
                        output.add("Difference: " + ratio);
                        System.out.print("Number of terms: ");
                        int termsGeo = input.nextInt();
                        output.add("Terms: " + termsGeo);
                        sum = SeriesCategory.geometricSeries(startGeo, ratio, termsGeo);
                        break;
                    case FIBONACCI:
                        System.out.print("Number of terms: ");
                        int termsFibo = input.nextInt();
                        output.add("Terms: " + termsFibo);
                        sum = SeriesCategory.fibonacciSeries(termsFibo);
                        break;
                    case FACTORIAL:
                        System.out.print("Starting int: ");
                        int startFact = input.nextInt();
                        output.add("Start: " + startFact);
                        sum = SeriesCategory.factorialSeries(startFact);
                        break;   
                }
                output.add("Sum: " + sum);
            }
            catch(IllegalArgumentException e) {
                System.out.println("Invalid series");
            }
        }

        try {  
            BufferedWriter buffWrite = new BufferedWriter(new FileWriter("output.txt"));
            for (String line : output){
                buffWrite.write(line);
                buffWrite.newLine();
            }
            buffWrite.close();
        }
        catch (FileNotFoundException e){
            System.out.println("File not found");
        } 
        catch (IOException ex) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}