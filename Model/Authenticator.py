from Model.Database import Database as db
from Model.Person import Person 

class Authenticator:
    def __init__(self):
        # Object of person class
        self.pr = None

        # Object of the database class
        self.database = db()
        self.database.connectToDataBase()
        self.cursor = self.database.getCursor()

    def isAuth(self, email, password):
        rows = self.database.executeQuery("SELECT * FROM person")
        column_names = [desc[0] for desc in self.database.getCursor().description]
        
        email_index    = column_names.index("email")
        password_index = column_names.index("passwordHash")

        for row in rows:
            if row[email_index] == email:
                if row[password_index] == password:
                    return True
        return False

    # Make a function here that returns the data of the student if the email and password are correct
    def returnPersonData(self, email, password):
        rows = self.database.executeQuery("SELECT * FROM person")
        column_names = [desc[0] for desc in self.database.getCursor().description]
        
        if self.isAuth(email, password):
            id_index          = column_names.index("personID")
            Fname_index       = column_names.index("firstName")
            Lname_index       = column_names.index("lastName")
            phone_index       = column_names.index("phoneNumber")
            sex_index         = column_names.index("sex")
            isAdmin_index     = column_names.index("isAdmin")
            dateOfBirth_index = column_names.index("dateOfBirth")
            email_index       = column_names.index("email")
            password_index    = column_names.index("passwordHash")

            for row in rows:
                if row[email_index] == email:
                    if row[password_index] == password:
                        self.pr = Person(
                            id = row[id_index],
                            firstName = row[Fname_index],
                            lastName = row[Lname_index],
                            number = row[phone_index],
                            sex = row[sex_index],
                            isAdmin = row[isAdmin_index],
                            dob = row[dateOfBirth_index],
                            email = row[email_index],
                            password = row[password_index]
                        )
        return self.pr

    def addPerson(self, newPerson: Person):

        query = "INSERT INTO PERSON (firstName, lastName, phoneNumber, dateOfBirth, sex, isAdmin, email, passwordHash) "
        query += "VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

        values = (newPerson.firstName, newPerson.lastName, newPerson.number, newPerson.dob, newPerson.sex, newPerson.isAdmin, newPerson.email, newPerson.password)

        self.cursor.execute(query, values)
        self.database.connectionHead.commit()
        
        return True
    
    def updatePerson(self, updatedPerson: Person):

        query =  "UPDATE Person "
        query += "SET firstName   = '{0}', ".format(updatedPerson.firstName)
        query += "    lastName    = '{0}', ".format(updatedPerson.lastName)
        query += "    phoneNumber = '{0}', ".format(updatedPerson.number)
        query += "    dateOfBirth = '{0}', ".format(updatedPerson.dob)
        query += "    sex         = '{0}', ".format(updatedPerson.sex)
        query += "    isAdmin     = '{0}', ".format(updatedPerson.isAdmin)
        query += "    email       = '{0}', ".format(updatedPerson.email)
        query += "    passwordHash= '{0}' ".format(updatedPerson.password)
        query += "WHERE personID  = {0}".format(updatedPerson.id)


        self.cursor.execute(query)
        self.database.connectionHead.commit()

        return True

