package bin;

import java.util.Scanner;
import src.*;

public class curVis 
{
 
    public static void main(final String[] args) {
        Welcome intro = new Welcome();
        String fname = intro.show();

        MainMenu options = new MainMenu();
        int selection = options.choice();

        if (selection == 4) {
            System.out.println("Thank you " + fname + " for using Currency Visualization program. We hope to see you some time soon");
            System.exit(0);
        }

        SubMenu subOptions = new SubMenu();

        switch(selection) {
            case 1:
                int subSelection = subOptions.subDailyChoice();
                break;
            case 2:
                subSelection = subOptions.subMonthlyChoice();
                break;
            case 3:
                subSelection = subOptions.subYearlyChoice();
                break;
            default:
                System.out.println("You haven't chosen any proper option!");
            
        //System.out.println(subSelection);
        }


        //int subSelection = subOptions.subChoice();
        
    }
}

