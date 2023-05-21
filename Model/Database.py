"""
IMPORTANT FOR THIS TO WORK:

INSTALL pyodbc (pip install pyodbc)

after installing find out the name of the server and the database you want to connect to
use this query to find out the server name:
    SELECT @@SERVERNAME

"""

# database object
import pyodbc
import sys

class Database:
    def __init__(self):
        self._db = None
        self.serverName = None
        self.databaseName = None
        self.cursor = None


    def connectToDataBase(self):
        #used to connect to the database
        #this function will ask the user for the server name and the database name
        
        # input("Enter the server name: ")
        self.serverName = "DESKTOP-VHJ2UQ7\SQLEXPRESS"

        # input("Enter the database name: ")
        self.databaseName = "library"
        
        connection_string = f"""
        DRIVER={"SQL SERVER"};
        SERVER={self.serverName};
        DATABASE={self.databaseName};
        Trust_Connection=yes;
        """
        try:
            cnxn = pyodbc.connect(connection_string)
            self.cursor = cnxn.cursor()
            # confirmation message 
        except Exception as e:
            print(e)
            print("Task is Terminated!")
            sys.exit(0)



    def closeConnection(self):
        self.cursor.close()

    def executeQuery(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getCursor(self):
        return self.cursor
    
    
    
