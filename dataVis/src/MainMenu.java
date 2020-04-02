package src;

import java.util.Scanner;

public class MainMenu 
{
    String firstOption = "1. View daily values";
    String secondOption = "2. View monthly average values";
    String thirdOption = "3. View yearly average values";
    String fourthOption = "4. View differences between values";
    String fifthOption = "5. Quit application\n";

    public int choice() {
        System.out.println(firstOption);
        System.out.println(secondOption);
        System.out.println(thirdOption);
        System.out.println(fourthOption);
        System.out.println(fifthOption);
        Scanner choice = new Scanner(System.in);
        System.out.print("Select the option: ");
        final int option = choice.nextInt();
        return option;
    }
}