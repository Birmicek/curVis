package src;

import java.util.Scanner;

public class Welcome {
    public String show() {
        Scanner input = new Scanner(System.in);
        System.out.print("Hello, please tell us your name: ");
        final String fname = input.next();
        System.out.println("\nWelcome to Currency Visualization program, " + fname + ".\n");
        System.out.println("This program shows currency rates of EUR upon other world currencies. The data is present since 04-th of January 1999. It is possible to view individual values per day, monthly and yearly averages, differences between values and more which you are about to discover within the self-help menu below:\n");
        return fname;
    }

}