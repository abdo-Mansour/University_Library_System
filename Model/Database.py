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
        # Some other example server values are
        # server = 'localhost\sqlexpress' # for a named instance
        # server = 'myserver,port' # to specify an alternate port
        # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
        # ask the user for the server name and database name
        self.serverName = input("Enter the server name: ")
        self.databaseName = input("Enter the database name: ")
        
        connection_string = f"""
        DRIVER={"SQL SERVER"};
        SERVER={self.serverName};
        DATABASE={self.databaseName};
        Trust_Connection=yes;
        """
        try:
            cnxn = pyodbc.connect(connection_string)
            self.cursor = cnxn.cursor()
        except Exception as e:
            print(e)
            print("Task is Terminated!")
            sys.exit(0)

    def closeConnection(self):
        self.cursor.close()

    def executeQuery(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        while row:
            print(row)
            row = self.cursor.fetchone()
