# Warning: MVC Pattern is applied here, DO NOT RETURN BOOK Object for example
# Only Pass data to viewer, not objects

from Model.Person import Person
from Model.Authenticator import Authenticator 
from Model.Library import Library


class Controller:
    def __init__(self):
        self.Person = None
        self.loggedIn = False
        self.Library = None
        self.auth = Authenticator()
        pass

    # Functions related to normal user query
    def logIn(self, email, password):       # DONE

        # Returns Exceptions if something wrong happened or true if success
        if self.auth.isAuth(email, password):
            self.Person = self.auth.returnPersonData(email, password)
            self.loggedIn = True
            # View should take true and display it as signed in
            return True
        else:
            # View should take false and display it as error
            return False

    def getBooksBy(self, query, value):     # DONE

        if self.loggedIn == True:
            queries = ["bookGenre", "author", "authorsOfBook", "location"]

            if query in queries:

                # this function should return a list of lists
                data = Library.getBooksBy(query, value)

                # View should display this returned data, also the data should be returned as a list
                return data
            else:

                # This should be displayed to the user as no books found
                return False

    def getNBooks(self, book):              # DONE

        # returns dictionary where every sub-list has all the data of the book
        if self.loggedIn == True:
            data = Library.getNBooks(book.id)
            if data:
                return data
            else:
                return False

    def getLocation(self, bookID):          # NOT DONE

        # returns location of the book
        if self.loggedIn == True:
            # I dont know how to fully implement this yet rn cause there are no functions in the database for this
            pass
        pass

    def getUserDetails(self):               # DONE
        if self.loggedIn == True:
            # Returns all data of user as a dictionary for view to use
            return self.Person.__dict__

    # Functions related to Admin Only Use
    def addStudent(self, studentInfo):      # DONE

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

            # returns a list where data is [id, firstName, lastName, number, dob, sex, isAdmin, email, password]
            self.auth.addStudent(newUser)

    def addBook(self, listOfBookDetails):   # DONE
        Library.addBook(listOfBookDetails)
        return True

    def updateBookDetails(self, bookInfo):  # NOT DONE
        # updates the book details
        pass

    def updateUserDetails(self, userInfo):  # NOT DONE
        # like the login, throws exception if the data entered is not valid
        pass
