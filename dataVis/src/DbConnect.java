package src;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.Statement;
import java.util.Properties;

public class DbConnect {
    String url = "jdbc:postgresql://localhost/postgres";
    // Properties props = new Properties();
    // props.setProperty("user","postgres");
    // props.setProperty("password","postgres");
    private String user= "postgres";
    private String password = "postgres"; 

    public void execute() {
        try {
            Connection conn = DriverManager.getConnection(url, user, password);
            Statement st = conn.createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM osboxes ORDER BY id DESC LIMIT 10");
            // ResultSetMetaData md = rs.getMetaData();
            // int colCount = md.getColumnCount();

            while (rs.next()) {
                System.out.println(rs.getString(1));
                
            }
            rs.close();
            st.close();
            
        } 
        catch (Exception e) {
            System.out.println(e);
        }
        
    }
}