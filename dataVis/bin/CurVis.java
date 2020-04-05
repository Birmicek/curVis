package bin;

import java.util.Scanner;
import src.*;

public class CurVis 
{
    public static String fname;
    public static int selection;
    public static int subSelection;

    public static void main(String[] args) {
        Welcome intro = new Welcome();
        fname = intro.show();

        MainMenu options = new MainMenu();
        selection = options.choice();

        if (selection == 4) {
            System.out.println("Thank you " + fname + " for using Currency Visualization program. We hope to see you some time soon");
            System.exit(0);
        }

        SubMenu subOptions = new SubMenu();

        switch(selection) {
            case 1:
                subSelection = subOptions.subDailyChoice();
                break;
            case 2:
                subSelection = subOptions.subMonthlyChoice();
                break;
            case 3:
                subSelection = subOptions.subYearlyChoice();
                break;
            default:
                System.out.println("You haven't chosen any proper option!");
        }
        
        SpecificSelection sel = new SpecificSelection();
        sel.selection();

        DbConnect connection = new DbConnect();
        connection.execute();
        
    }
}

