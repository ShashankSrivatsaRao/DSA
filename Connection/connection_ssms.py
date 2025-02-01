#Conncecting to sql server using python
import pypyodbc as odbc # type: ignore # Import the module

DRIVER_NAME = 'SQL Server'
SERVER_NAME = 'DESKTOP-RUEBP2D\SQLEXPRESS'
DATABASE_NAME = 'PREP'

# uid=DESKTOP-RUEBP2D\shash

connection_string = f"""
        DRIVER={{{DRIVER_NAME}}}; 
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trusted_Connection=yes;
        
        """
conn = odbc.connect(connection_string) # Connect to the database
print(conn) # Print the connection object