package src;

import java.util.Scanner;

public class SubMenu
{
    String firstSubOption = "1. View 1 or more different values for 1 or more currencies";
    String secondSubOption = "2. View range of values for 1 or more currencies";

    public int subDailyChoice() {
        System.out.println("=============================");
        System.out.println("\nYou have chosen DAILY values. Please choose now your further step:\n");
        System.out.println(firstSubOption);
        System.out.println(secondSubOption);
        Scanner subChoice = new Scanner(System.in);
        System.out.print("\nSelect the option: ");
        final int subOption = subChoice.nextInt();
        return subOption;
    }

    public int subMonthlyChoice() {
        System.out.println("=============================");
        System.out.println("\nYou have chosen MONTHLY values. Please choose now your further step:\n");
        System.out.println(firstSubOption);
        System.out.println(secondSubOption);
        Scanner subChoice = new Scanner(System.in);
        System.out.print("\nSelect the option: ");
        final int subOption = subChoice.nextInt();
        return subOption;
    }

    public int subYearlyChoice() {
        System.out.println("=============================");
        System.out.println("\nYou have chosen YEARLY values. Please choose now your further step:\n");
        System.out.println(firstSubOption);
        System.out.println(secondSubOption);
        Scanner subChoice = new Scanner(System.in);
        System.out.print("\nSelect the option: ");
        final int subOption = subChoice.nextInt();
        return subOption;
    }
}