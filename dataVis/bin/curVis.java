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

        if (selection == 5) {
            System.out.println("Thank you " + fname + " for using Currency Visualization program. We hope to see you some time soon");
            System.exit(0);
        }
        else {
            //Code to be added
            System.out.println("Please continue");
        }
        
    }
}

