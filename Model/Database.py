"""
IMPORTANT FOR THIS TO WORK:
1. INSTALL Microsoft ODBC Driver 17 for SQL Server (check if you have it already)
2. INSTALL pyodbc (pip install pyodbc)

"""

# database object
import pyodbc


class Database:
    def __init__(self):
        self._db = None
        self.serverName = 'LAPTOP-F2RRO5TA'
        self.databaseName = 'Toffee'
        self.userName = 'root'
        self.password = 'pass'
        self.cursor = None

    def connectToDataBase(self):
        # Some other example server values are
        # server = 'localhost\sqlexpress' # for a named instance
        # server = 'myserver,port' # to specify an alternate port
        # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.serverName +
                              ';DATABASE='+self.databaseName+';ENCRYPT=yes;UID='+self.userName+';PWD=' + self.password)
        self.cursor = cnxn.cursor()

    def closeConnection(self):
        self.cursor.close()

    def executeQuery(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        while row:
            print(row)
            row = self.cursor.fetchone()
