package src;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.Statement;
import java.util.Arrays;

public class DbConnect {
    private String url = "jdbc:postgresql://localhost/postgres";
    private String user= "postgres";
    private String password = "postgres";
    String sql;
    String inpIndCurr = Arrays.toString(SpecificSelection.inpIndCurr).replace("[", "").replace("]", "");
    String inpRangeCurr = Arrays.toString(SpecificSelection.inpRangeCurr).replace("[", "").replace("]", "");
    String inpIndDates = Arrays.toString(SpecificSelection.inpIndDates).replace("[", "('").replace("]", "')").replace(", ", "', '");
    String startRanDate = SpecificSelection.startRanDate;
    String endRanDate = SpecificSelection.endRanDate;
    
    

    public void setSql() {
        if (!inpIndCurr.contains("null") && !inpIndCurr.isEmpty() && !inpIndDates.contains("null") && !inpIndDates.isEmpty()) {
            if (inpIndCurr.contains("all")) {
                sql = "SELECT * FROM osboxes WHERE date IN " + inpIndDates;
            }
            else {
                sql = "SELECT id,date," + inpIndCurr + " FROM osboxes WHERE date IN " + inpIndDates;
            }
        }
        else if (!inpRangeCurr.contains("null") && !inpRangeCurr.isEmpty() && !startRanDate.contains("null") && !startRanDate.isEmpty() && !endRanDate.contains("null") && !endRanDate.isEmpty()){
            if (inpRangeCurr.contains("all")) {
                sql = "SELECT * FROM osboxes WHERE date BETWEEN '" + startRanDate + "' AND '" + endRanDate + "'";
            }
            else {
                sql = "SELECT id,date," + inpRangeCurr + " FROM osboxes WHERE date BETWEEN '" + startRanDate + "' AND '" + endRanDate + "'";
            }
        }
            
        else {
            sql = "SELECT * FROM osboxes ORDER BY id LIMIT 10";
            System.out.println("You haven't chosen proper values as inputs, therefore default output will be shown\n");
        }
    } 
    

    public void execute() {
        try {
            Connection conn = DriverManager.getConnection(url, user, password);
            Statement st = conn.createStatement();
            ResultSet rs = st.executeQuery(sql);
            ResultSetMetaData md = rs.getMetaData();
            int colCount = md.getColumnCount();         
            
            System.out.println("\nSee below your requested data: \n");
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