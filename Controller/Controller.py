# Warning: MVC Pattern is applied here, DO NOT RETURN BOOK Object for example
# Only Pass data to viewer, not objects


from Model.Book import Book
from Model.Person import Person
from Model.Library import Library
from Model.Authenticator import Authenticator


class Controller:
    def __init__(self):
        self.Person = None
        self.Library = Library()
        self.auth = Authenticator()
        self.loggedIn = True
        self.isAdmin = True

    # Functions related to normal user query
    def login(self, email, password, isAdmin):       # DONE

        # Returns Exceptions if something wrong happened or true if success
        if self.auth.isAuth(email, password):
            self.Person = self.auth.returnPersonData(email, password)

            self.isAdmin = True if self.Person.isAdmin else False
            # checks if the user is an admin or not
            if ((self.isAdmin == False and isAdmin == True) or (self.isAdmin == True and isAdmin == False)):
                return False

            self.loggedIn = True

            # View should take true and display it as signed in
            return True
        else:
            # View should take false and display it as error
            return False

    def getBooksBy(self, query, value):     # DONE

        if self.loggedIn:
            queries = ['Title', 'PageCount', 'ISBN', 'Language', 'Description',
                       'Publisher', 'MinimumAgeToRead', 'PublicationYear']

            if query in queries:

                bookCollection = []
                # this function should return a list of books
                data = self.Library.getBooksBy(query, value)
                for book in data:
                    bookDic = {}
                    bookDic['BookID'] = book.BookID
                    bookDic['Title'] = book.Title
                    bookDic['ISBN'] = book.ISBN
                    bookDic['PageCount'] = book.PageCount
                    bookDic['Language'] = book.Language
                    bookDic['Description'] = book.Description
                    bookDic['Publisher'] = book.Publisher
                    bookDic['MinAgeToRead'] = book.MinAgeToRead
                    bookDic['PublicationYear'] = book.PublicationYear
                    bookCollection.append(bookDic)

                # View should display this returned data, also the data should be returned as a list of dictionaries
                return bookCollection
            else:

                # This should be displayed to the user as no books found
                return False
        else:
            return False

    def getNBooks(self):              # SEMI DONE
        # return a list of book dictionaries
        N = 100
        offset = 0    # Need to put values for these
        if self.loggedIn:
            try:
                bookCollection = self.Library.getNBooks(self, N, offset)
                data = []
                for book in bookCollection:
                    bookDic = {}
                    bookDic['BookID'] = book.BookID
                    bookDic['Title'] = book.Title
                    bookDic['ISBN'] = book.ISBN
                    bookDic['PageCount'] = book.PageCount
                    bookDic['Language'] = book.Language
                    bookDic['Description'] = book.Description
                    bookDic['Publisher'] = book.Publisher
                    bookDic['MinAgeToRead'] = book.MinAgeToRead
                    bookDic['PublicationYear'] = book.PublicationYear
                    data.append(bookDic)
                return data
            except:
                return False
        else:
            return False

    def getAllBooks(self):
        if self.loggedIn:
            try:
                bookCollection = self.Library.getAllBooks()
                data = []
                for book in bookCollection:
                    bookDic = {}
                    bookDic['BookID'] = book.BookID
                    bookDic['Title'] = book.Title
                    bookDic['ISBN'] = book.ISBN
                    bookDic['PageCount'] = book.PageCount
                    bookDic['Language'] = book.Language
                    bookDic['Description'] = book.Description
                    bookDic['Publisher'] = book.Publisher
                    bookDic['MinAgeToRead'] = book.MinAgeToRead
                    bookDic['PublicationYear'] = book.PublicationYear
                    data.append(bookDic)
                return data
            except:
                return False
        else:
            return False

    def getUserDetails(self):               # DONE
        if self.loggedIn:
            # Returns all data of user as a dictionary for view to use
            return self.Person.__dict__
        else:
            return False

    def getLocation(self, ISBN, copyID):          # DONE
        # returns location of the book as dictionary
        if self.loggedIn:
            try:
                location = self.Library.getBookCopyLocation(ISBN, copyID)
                return location.__dict__
            except:
                return False
        else:
            return False

    def updateUserDetails(self, personInfo):  # DONE
        if self.loggedIn:
            updatedPerson = Person(
                id=personInfo[0],
                firstName=personInfo[1],
                lastName=personInfo[2],
                number=personInfo[3],
                dob=personInfo[4],
                sex=personInfo[5],
                isAdmin=personInfo[6],
                email=personInfo[7],
                password=personInfo[8]
            )

            if (self.auth.updatePerson(updatedPerson)):
                return True
            else:
                return False
        else:
            return False

    # Functions related to Admin Only Use
    def addUser(self, userInfo):      # DONE
        # This is to check if the user is both LOGGED IN and IS AN ADMIN, because this function is only for admins
        if self.loggedIn and self.isAdmin:
            newUser = Person(
                firstName=userInfo[0],
                lastName=userInfo[1],
                number=userInfo[2],
                dob=userInfo[3],
                sex=userInfo[4],
                isAdmin=userInfo[5],
                email=userInfo[6],
                password=userInfo[7]
            )

            if (self.auth.addPerson(newUser)):
                return True
            else:
                return False
        else:
            return False

    def addBook(self, listOfBookDetails):   # DONE
        if self.loggedIn and self.isAdmin:
            try:
                book = Book(
                    Title=listOfBookDetails[0],
                    ISBN=listOfBookDetails[1],
                    PageCount=listOfBookDetails[2],
                    Language=listOfBookDetails[3],
                    Description=listOfBookDetails[4],
                    Publisher=listOfBookDetails[5],
                    MinAgeToRead=listOfBookDetails[6],
                    PublicationYear=listOfBookDetails[7]
                )
                self.Library.addBook(book)
                return True
            except:
                return False
        else:
            return False

    def updateBookDetails(self, bookInfo):  # DONE
        if self.loggedIn and self.isAdmin:
            try:
                book = Book(
                    BookID=bookInfo[0],
                    Title=bookInfo[1],
                    PageCount=bookInfo[2],
                    ISBN=bookInfo[3],
                    Language=bookInfo[4],
                    Description=bookInfo[5],
                    Publisher=bookInfo[6],
                    MinAgeToRead=bookInfo[7],
                    PublicationYear=bookInfo[8]
                )

                if (self.Library.updateBookDetails(book)):
                    return True
                else:
                    return False
            except:
                return False
        else:
            return False

    def generateStatisticsReport(self):
        report = {"nBooks": int(self.Library.getNoOfBooks()[0][0]),
                  "nBooksForEveryGenre": self.Library.getNoOfBooksForEveryGenre(),
                  "nBooksForEveryLang": self.Library.getNoOfBooksForEveryLang(),
                  "nStudents": int(self.Library.getNoOfStudents()[0][0])}
        return report

    def deleteBook(self, ISBN):
        if self.loggedIn and self.isAdmin:
            if (self.Library.deleteBook(ISBN)):
                return True
            else:
                return False
        else:
            return False

    def deleteUser(self, userEmail):

        if self.loggedIn and self.isAdmin:
            if (self.Library.deleteUser(userEmail)):
                return True
            else:
                return False
        else:
            return False

    def addBookGenre(self, ISBN, genre):
        if self.loggedIn and self.isAdmin:
            self.Library.addBookGenre(ISBN, genre)
        else:
            return False
    
    def addBookCopy(self, ISBN, floor , section , shelfNumber , numberOfCopies):
        if self.loggedIn:
            self.Library.addBookCopy(ISBN, floor , section , shelfNumber , numberOfCopies)
        else:
            return False

    # def borrowBook(self, ISBN, copyID , userID): #TODO:
    #     pass

    # def returnBook(self, ISBN, copyID , userID): #TODO:
    #     pass
