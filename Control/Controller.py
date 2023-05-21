# Warning: MVC Pattern is applied here, DO NOT RETURN BOOK Object for example
# Only Pass data to viewer, not objects

from Model.Person import Person
from Model.Authenticator import Authenticator 


class Controller:
    def __init__(self):
        self.Person = None
        self.loggedIn = False
        self.library
        self.ath = Authenticator()
        pass

    # Functions related to normal user query
    def logIn(self, email, password):
        # Returns Exceptions if something wrong happened or true if success
        if self.ath.isAuth(email, password):
            self.Person = self.ath.returnPersonData(email, password)
            self.loggedIn = True
            # View should take true and display it as signed in
            return True
        else:
            # View should take false and display it as error
            return False

    def getBooksBy(self, query, value):

        if self.loggedIn == True:
            queries = ["bookGenre", "author", "authorsOfBook", "location"]

            if query in queries:

                # this function should return a list of lists
                data = checkDatabase(query, value)

                # View should display this returned data, also the data should be returned as a list
                return data
            else:

                # This should be displayed to the user as no books found
                return False

        """
        Returns list of lists under given query and value

        Parameters:
        self : self
        query (string): the attribute you want to search about, for example "author"
        value (string): the value of the attribute you want to search about, for example "El-Messery"

        Returns:
        int: list of lists where every sub-list has all the data of the book under given category
        """
        pass

    def getNBooks(self, book):
        # returns dictionary where every sub-list has all the data of the book
        if self.loggedIn == True:
            data = getDetails(book.id)
            if data:
                return data
            else:
                return False

    def getLocation(self, bookID):
        # returns location of the book
        if self.loggedIn == True:
            # I dont know how to fully implement this yet rn cause there are no functions in the database for this
            pass
        pass

    def getUserDetails(self):
        if self.loggedIn == True:
            return self.Person

    def addStudent(self, studentInfo):
        # Functions related to Admin Only Use
        # studentInfo should be a list where data is [id, firstName, lastName, number, dob, sex, isAdmin, email, password]
        if self.loggedIn and self.isAdmin:
            newUser = Person(
                id=studentInfo[0],
                firstName=studentInfo[1],
                lastName=studentInfo[2],
                number=studentInfo[3],
                dob=studentInfo[4],
                sex=studentInfo[5],
                isAdmin=studentInfo[6],
                email=studentInfo[7],
                password=studentInfo[8]
            )

            self.ath.addStudent(newUser)

    def addBook(self, listOfBookDetails):
        # like the login, throws exception if the data entered is not valid
        pass

    def updateBookDetails(self, bookInfo):
        # updates the book details
        pass

    def updateUserDetails(self, userInfo):
        # like the login, throws exception if the data entered is not valid
        pass
