"""
IMPORTANT FOR THIS TO WORK:

INSTALL pyodbc (pip install pyodbc)

after installing find out the name of the server and the database you want to connect to
use this query to find out the server name:
    SELECT @@SERVERNAME

"""

import pyodbc
import sys


# database object
class Database:
    def __init__(self):
        self.__serverName = None
        self.databaseName = None
        self.cursor = None
        self.__username = None
        self.__password = None
        self.__driver = None

    def connectToDataBase(self):
        # used to connect to the database
        # this function will ask the user for the server name and the database name

        self.__serverName = 'SQL8005.site4now.net'

        self.databaseName = 'db_a99989_librarysystem'

        self.__username = 'db_a99989_librarysystem_admin'

        self.__password = '$SzbsB6C1lte'

        self.__driver = '{ODBC Driver 17 for SQL Server}'

        connection_string = f"""
        DRIVER={self.__driver};
        SERVER={self.__serverName};
        DATABASE={self.databaseName};
        UID={self.__username};
        PWD={self.__password};
        Trust_Connection=yes;
        """
        try:
            cnxn = pyodbc.connect(connection_string)
            self.cursor = cnxn.cursor()
            # confirmation message
        except Exception as e:
            print(e)
            print("Connection To Data Base failed, make sure you have internet connection.")
            sys.exit(0)

    def closeConnection(self):
        self.cursor.close()

    def executeQuery(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getCursor(self):
        return self.cursor
