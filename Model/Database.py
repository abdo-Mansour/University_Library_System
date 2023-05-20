"""
IMPORTANT FOR THIS TO WORK:
1. INSTALL Microsoft ODBC Driver 17 for SQL Server (check if you have it already)
2. INSTALL pyodbc (pip install pyodbc)

try:
        conn = odbc.connect(connection_string)
    except Exception as e:
        print(e)
        print("Task is Terminated!")
        sys.exit(0)

    return conn
"""

# database object
import pyodbc


class Database:
    def __init__(self):
        self._db = None
        self.serverName = 'LAPTOP-F2RRO5TA'
        self.databaseName = 'Toffee'
        self.cursor = None

    def connectToDataBase(self):
        # Some other example server values are
        # server = 'localhost\sqlexpress' # for a named instance
        # server = 'myserver,port' # to specify an alternate port
        # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
        connection_string = f"""
        DRIVER={"SQL SERVER"};
        SERVER={self.serverName};
        DATABASE={self.databaseName};
        Trust_Connection=yes;
        """
        cnxn = pyodbc.connect(connection_string)
        self.cursor = cnxn.cursor()

    def closeConnection(self):
        self.cursor.close()

    def executeQuery(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        while row:
            print(row)
            row = self.cursor.fetchone()
