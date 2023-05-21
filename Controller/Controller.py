# Warning: MVC Pattern is applied here, DO NOT RETURN BOOK Object for example
# Only Pass data to viewer, not objects
# ALL PRINT STATEMENTS MUST BE REMOVED


from Model.Person import Person
from Model.Authenticator import Authenticator 
from Model.Library import Library, Book

class Controller:
    def __init__(self):
        self.Person = None
        self.Library = None
        self.auth = Authenticator()
        self.loggedIn = False
        self.isAdmin = False

    # Functions related to normal user query
    def logIn(self, email, password):       # DONE

        # Returns Exceptions if something wrong happened or true if success
        if self.auth.isAuth(email, password):
            self.Person = self.auth.returnPersonData(email, password)

            self.isAdmin = True if self.Person.isAdmin else False
            self.loggedIn = True
            
            # View should take true and display it as signed in
            return True
        else:
            # View should take false and display it as error
            return False

    def getBooksBy(self, query, value):     # DONE

        if self.loggedIn:
            queries = ["bookGenre", "author", "ISBN", "title", "pageCount", "language", "publisher", "publicationYear"]

            if query in queries:

                # this function should return a list of lists
                data = Library.getBooksBy(query, value)

                # View should display this returned data, also the data should be returned as a list
                return data
            else:

                # This should be displayed to the user as no books found
                return False
        else:
            print("You're not logged in")

    def getNBooks(self, book):              # SEMI DONE
        # return a list of book dictionaries
        N, offset = None    # Need to put values for these
        if self.loggedIn:
            try:
                bookCollection = Library.getNBooks(self, N, offset)
                data = []
                for books in bookCollection:
                    data.append(books.__dict__)
                return data
            except:
                print("Error getting data")
        else:
            print("You're not logged in")

    def getUserDetails(self):               # DONE
        if self.loggedIn:
            # Returns all data of user as a dictionary for view to use
            return self.Person.__dict__
        else:
            print("You're not logged in")

    
    def getLocation(self, bookID , copyID):          # DONE
        # returns location of the book as dictionary
        if self.loggedIn:
            try:
                location = Library.getBookCopyLocation(self,bookID, copyID)
                return location.__dict__
            except:
                print("Error retrieving book data")
        else:
            print("You're not logged in")

    # Functions related to Admin Only Use
    def addStudent(self, studentInfo):      # DONE
        # This is to check if the user is both LOGGED IN and IS AN ADMIN, because this function is only for admins
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
            self.auth.addPerson(newUser)
        else:
            print("Sorry you're not an admin")

    def addBook(self, listOfBookDetails):   # DONE
        if self.loggedIn and self.isAdmin:
            try:
                Library.addBook(listOfBookDetails)
                return True
            except:
                print("Failed to add book to database")
                return False
        else:
            print("Sorry you're not an admin")

    def updateBookDetails(self, bookInfo):  # DONE
        if self.loggedIn and self.isAdmin:
            try:
                Library.updateBookDetails(bookInfo)
            except:
                print("Error updating book details")
        else:
            print("Sorry you're not an admin")

    def updateUserDetails(self, personInfo):  # DONE
        if self.loggedIn and self.isAdmin:
            updatedPerson = Person(
                id       = personInfo[0],
                firstName= personInfo[1],
                lastName = personInfo[2],
                number   = personInfo[3],
                dob      = personInfo[4],
                sex      = personInfo[5],
                isAdmin  = personInfo[6],
                email    = personInfo[7],
                password = personInfo[8]
            )
            self.auth.updatePerson(updatedPerson)
        else:
            print("Sorry you're not an admin")