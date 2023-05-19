# Warning: MVC Pattern is applied here, DO NOT RETURN BOOK Object for example
# Only Pass data to viewer, not objects


class Controller:
    def __init__(self):
        self.authenticator
        self.library
        pass

    # Functions related to normal user querey
    def logIn(self, email, password):
        # Returns Exceptions if something wrong happend or true if success
        pass

    def getBooksUnder(self, query, value):
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

    def getNBooks(self, n):
        # returns list of lists where every sub-list has all the data of the book
        pass

    def getLocation(self, bookID):
        # returns location of the book
        pass

    def getUserDetails(self):
        pass

    def addStudent(self, studentInfo):
        # Functions related to Admin Only Use
        pass

    def addBook(self, listOfBookDetails):
        # like the login, throws exception if the data entered is not valid
        pass

    def updateBookDetails(self, bookID, bookInfo):
        # updates the book details
        pass

    def updateUserDetails(self , userInfo):
        # like the login, throws exception if the data entered is not valid
        pass


