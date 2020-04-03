package src;

import java.util.Scanner;
import src.MainMenu;

public class SubMenu extends MainMenu
{
    String firstSubOption = "1. View 1 value";
    String secondSubOption = "2. View range of values";
    String thirdSubOption = "3. View more different values";

    public int subDailyChoice() {
        System.out.println("\nYou have chosen DAILY values. Please choose now your further step:\n");
        System.out.println(firstSubOption);
        System.out.println(secondSubOption);
        System.out.println(thirdSubOption);
        Scanner subChoice = new Scanner(System.in);
        System.out.print("\nSelect the option: ");
        final int subOption = subChoice.nextInt();
        return subOption;
    }

    public int subMonthlyChoice() {
        System.out.println("\nYou have chosen MONTHLY values. Please choose now your further step:\n");
        System.out.println(firstSubOption);
        System.out.println(secondSubOption);
        System.out.println(thirdSubOption);
        Scanner subChoice = new Scanner(System.in);
        System.out.print("\nSelect the option: ");
        final int subOption = subChoice.nextInt();
        return subOption;
    }

    public int subYearlyChoice() {
        System.out.println("\nYou have chosen YEARLY values. Please choose now your further step:\n");
        System.out.println(firstSubOption);
        System.out.println(secondSubOption);
        System.out.println(thirdSubOption);
        Scanner subChoice = new Scanner(System.in);
        System.out.print("\nSelect the option: ");
        final int subOption = subChoice.nextInt();
        return subOption;
    }

    public int subDifferenceChoice() {
        System.out.println("\nYou have chosen to view differences between 2 values. Please choose now your further step:\n");
        System.out.println(firstSubOption);
        System.out.println(secondSubOption);
        System.out.println(thirdSubOption);
        Scanner subChoice = new Scanner(System.in);
        System.out.print("\nSelect the option: ");
        final int subOption = subChoice.nextInt();
        return subOption;
    }
}