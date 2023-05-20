
import Model.Database as db

database = db.Database()
database.connectToDataBase()
database.executeQuery("SELECT * FROM \"User\"")

