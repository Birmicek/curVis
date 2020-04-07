package src;

import java.util.Scanner;
import bin.CurVis;

public class SpecificSelection {
    int selectedOption = CurVis.selection;
    int selectedSubOption = CurVis.subSelection;
    public static String[] inpIndCurr;
    public static String[] inpIndDates;
    public static String[] inpRangeCurr;
    public static String startRanDate;
    public static String endRanDate;
    String currencies = "USD, JPY, BGN, CYP, CZK, DKK, EEK, GBP, HUF, LTL, LVL, MTL, PLN, ROL, RON, SEK, SIT, SKK, CHF, ISK, NOK, HRK, RUB, TRL, TRY, AUD, BRL, CAD, CNY, HKD, IDR, ILS, INR, KRW, MXN, MYR, NZD, PHP, SGD, THB, ZAR";

    public void selection() {
        System.out.println("=============================");
        System.out.println("\nHere is a list of available currencies:\n" + currencies + "\n\nand example of a date format: 1999-01-22\n");
        
        switch(selectedOption) {
            case 1:
                switch(selectedSubOption){
                    case 1:
                        //View 1 or more different values for 1 or more currencies
                        Scanner indCur = new Scanner(System.in);
                        System.out.println("Please enter 1 or more currencies (from above list) separated by comma without space. Example: USD,JPY,CZK or type 'all' to see values for all currencies\n");
                        System.out.print("Currencies: ");
                        inpIndCurr = indCur.next().split(",");

                        Scanner indDates = new Scanner(System.in);
                        System.out.println("\nPlease enter 1 or more dates (in format as above) separated by comma without space. Example: 1999-01-22,2020-03-25 or type 'all' to see values for all dates\n");
                        System.out.print("Dates: ");
                        inpIndDates = indDates.next().split(",");
                        
                        // System.out.println(Arrays.toString(inpIndCurr));
                        // System.out.println(Arrays.toString(inpIndDates));
                        break;

                    case 2:
                        //View range of values for 1 or more currencies
                        Scanner rangeCurr = new Scanner(System.in);
                        System.out.println("Please enter 1 or more currencies (from above list) separated by comma without space. Example: USD,JPY,CZK or type 'all' to see values for all currencies\n");
                        System.out.print("Currencies: ");
                        inpRangeCurr = rangeCurr.next().split(",");

                        Scanner startDate = new Scanner(System.in);
                        System.out.println("\nPlease enter Start date of the date range. Example: 1999-01-22\n");
                        System.out.print("Start date: ");
                        startRanDate = startDate.next();

                        Scanner endDate = new Scanner(System.in);
                        System.out.println("\nPlease enter End date of the date range. Example: 2020-03-25\n");
                        System.out.print("End date: ");
                        endRanDate = endDate.next();

                        // System.out.println(Arrays.toString(inpRangeCurr));
                        // System.out.println(startRanDate);
                        // System.out.println(endRanDate);
                        break;
                        
                    default:
                        System.out.println("You haven't chosen any proper option");
                }
            default:
                return;
        }
    }
}