from Model.Database import Database as db
from Model.Person import Person 
import sys


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
                            row[id_index],
                            row[Fname_index],
                            row[Lname_index],
                            row[phone_index],
                            row[sex_index],
                            row[isAdmin_index],
                            row[dateOfBirth_index],
                            row[email_index],
                            row[password_index]
                        )
        return self.pr

    def addStudent(self, newStudent: Person):

        query = "INSERT INTO PERSON (firstName, lastName, phoneNumber, dateOfBirth, sex, isAdmin, email, passwordHash) "
        query += "VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

        values = (newStudent.firstName, newStudent.lastName, newStudent.number, newStudent.dob, newStudent.sex, newStudent.isAdmin, newStudent.email, newStudent.password)

        self.cursor.execute(query, values)
        self.database.connectionHead.commit()
        
        print("Student has benn Added Successfully")
