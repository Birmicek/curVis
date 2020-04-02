package src;

public class MainMenu 
{
    String firstOption = "1. View daily values";
    String secondOption = "2. View monthly average values";
    String thirdOption = "3. View yearly average values";
    String fourthOption = "4. View differences between values";
    String fifthOption = "5. Quit application";

    public void show() {
        System.out.println(firstOption);
        System.out.println(secondOption);
        System.out.println(thirdOption);
        System.out.println(fourthOption);
        System.out.println(fifthOption);
    }
}