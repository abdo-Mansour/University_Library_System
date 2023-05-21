"""
IMPORTANT FOR THIS TO WORK:

INSTALL pyodbc (pip install pyodbc)
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
        
        # Used to connect to the database
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
            self.connectionHead = cnxn
            # confirmation message
            print("Connected to Database")
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
