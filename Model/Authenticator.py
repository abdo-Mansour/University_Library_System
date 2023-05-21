from Model.Database import Database as db
from Model.Person import Person as prs
import sys


class Authenticator:
    def __init__(self):
        # Object of person class
        self.pr = None
        print("---AUTHENTICATOR CLASS---")

        # Object of the database class
        self.database = db()
        self.database.connectToDataBase()

        # Retrieved query (default query)
        self.rows = self.database.executeQuery("SELECT * FROM person")

        # All of the person attributes names
        self.column_names = [desc[0]
                             for desc in self.database.getCursor().description]

    def isAuth(self, email, password):
        print("---IS AUTH FUNCTION IN AUTHOR. CLASS---")
        email_index = self.column_names.index("email")
        password_index = self.column_names.index("passwordHash")

        for row in self.rows:
            if row[email_index] == email:
                if row[password_index] == password:
                    return True
        return False

    # Make a function here that returns the data of the student if the email and password are correct
    def returnPersonData(self, email, password):
        if self.isAuth(email, password):
            id_index = self.column_names.index("personID")
            Fname_index = self.column_names.index("firstName")
            Lname_index = self.column_names.index("lastName")
            phone_index = self.column_names.index("phoneNumber")
            sex_index = self.column_names.index("sex")
            isAdmin_index = self.column_names.index("isAdmin")
            dateOfBirth_index = self.column_names.index("dateOfBirth")
            email_index = self.column_names.index("email")
            password_index = self.column_names.index("passwordHash")

            for row in self.rows:
                if row[email_index] == email:
                    if row[password_index] == password:
                        self.pr = prs.Person(
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

    def addStudent(self, newStudent: prs):
        # This print statements for testing
        print("---ADD STUDENT FUNCTION IN AUTHOR. CLASS---")
        print("student id: ", newStudent.id)
        print("student email: ", newStudent.email)
        print("student phone: ", newStudent.phone)
        query = f"INSERT INTO PERSON(firstName, lastName, phoneNumber, dateOfBirth, sex, isAdmin, email, passwordHash) Values({newStudent.id})"
        self.database.executeQuery("")
