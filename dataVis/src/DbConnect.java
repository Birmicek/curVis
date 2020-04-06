package src;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Properties;
import src.SpecificSelection;

public class DbConnect {
    private String url = "jdbc:postgresql://localhost/postgres";
    // Properties props = new Properties();
    // props.setProperty("user","postgres");
    // props.setProperty("password","postgres");
    private String user= "postgres";
    private String password = "postgres";
    String sql;
    String inpIndCurr = Arrays.toString(SpecificSelection.inpIndCurr).replace("[", "").replace("]", "");
    String inpIndDates = Arrays.toString(SpecificSelection.inpIndDates).replace("[", "('").replace("]", "')").replace(", ", "', '");
    

    public void setSql() {
        if (inpIndCurr.length() != 0 && inpIndDates.length() != 0) {
            sql = "SELECT id,date," + inpIndCurr + " FROM osboxes WHERE date IN " + inpIndDates;
        }
        else {
            sql = "SELECT * FROM osboxes ORDER BY id LIMIT10";
            System.out.println("You haven't chosen proper values as inputs, therefore default output will be shown");
        }
    } 
    

    public void execute() {
        try {
            Connection conn = DriverManager.getConnection(url, user, password);
            Statement st = conn.createStatement();
            ResultSet rs = st.executeQuery(sql);
            ResultSetMetaData md = rs.getMetaData();
            int colCount = md.getColumnCount();         
            
            System.out.println();

            for(int i = 1; i <= colCount; i++) {
                String colName = md.getColumnName(i);
                if(i == colCount) {
                    System.out.print(colName + "\n");
                }
                else {
                    System.out.print(colName + "\t");
                }
            }

            while (rs.next()) {
                for (int i = 1; i <= colCount; i++) {
                    if (i == colCount) {
                        System.out.print(rs.getString(i) + "\n");
                    }
                    else {
                        System.out.print(rs.getString(i) + "\t");
                    }
                }
                                
            }
            rs.close();
            st.close();
            
        } 
        catch (Exception e) {
            System.out.println(e);
        }
        
    }
}