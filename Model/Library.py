import Model.Database as db
import Model.Book as Book
import Model.Location as Location

class Library:
    def __init__(self):
        # This is used as the curser for the database
        self.database = db.Database()
        self.database.connectToDataBase()
        self.cursor = self.database.getCursor()

    def bookDataParse(self):
        rows = self.cursor.fetchall()
        booksList = []
        for row in rows:
            tempBook = Book.Book()
            for element, infoAtt in zip(row, tempBook.attributes):
                setattr(tempBook, infoAtt, element)
            booksList.append(tempBook)
        return booksList

    def getBooksBy(self, column, value):
        if column == 'genre':
            return self.getBookByGenre(value)
        if (column == 'author'):
            return self.getBooksByAuthor(value)
        query = f'SELECT * FROM Book WHERE {column} like ?'
        value = '%' + value + '%'
        self.cursor.execute(query, value)
        return self.bookDataParse()

    def getBooksByAuthor(self, authorID):
        query = "SELECT book.* FROM book, authorsOfBook WHERE book.bookID = authorsOfBook.bookID AND authorID = ?"
        self.cursor.execute(query, authorID)
        return self.bookDataParse()

    def getBookByGenre(self, genre):
        query = "SELECT book.* FROM book, bookGenre WHERE book.bookID = bookGenre.bookID AND genre = ?"
        self.cursor.execute(query, genre)
        return self.bookDataParse()

    def getNBooks(self, N, offset):
        query = "SELECT * FROM book ORDER BY bookID OFFSET ? ROWS FETCH NEXT ? ROWS ONLY;"
        self.cursor.execute(query, (offset, N))
        return self.bookDataParse()

    def getAllBooks(self):
        query = "SELECT * FROM book"
        self.cursor.execute(query)
        return self.bookDataParse()

    def addBook(self, book):
        attributes = ['Title', 'PageCount', 'ISBN', 'Language',
                      'Description', 'Publisher', 'MinAgeToRead', 'PublicationYear']
        query = "INSERT INTO book (Title, PageCount, ISBN, Language, Description, Publisher, MinimumAgeToRead, PublicationYear)"
        query += "VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)"
        valuesList = []
        for i in range(len(attributes)):
            valuesList.append(getattr(book, attributes[i]))
        tempTuple = tuple(valuesList)
        self.cursor.execute(query, tempTuple)
        self.database.connectionHead.commit()

    def updateBookDetails(self, updatedBook):
        # updated book is a book object that contains the updated book data
        attributes = ['Title', 'PageCount', 'ISBN', 'Language',
                      'Description', 'Publisher', 'MinAgeToRead', 'PublicationYear']
        query = "UPDATE book SET Title = ?, PageCount = ?, ISBN= ?, Language = ?,Description= ?, Publisher= ?, MinimumAgeToRead= ?, PublicationYear= ? WHERE bookID = ?"
        valuesList = []
        for i in range(len(attributes)):
            valuesList.append(getattr(updatedBook, attributes[i]))
        valuesList.append(updatedBook.BookID)
        tempTuple = tuple(valuesList)
        self.cursor.execute(query, tempTuple)
        self.database.connectionHead.commit()
        return True

    def getBookCopyLocation(self, bookID, copyID):
        query = "SELECT location.* FROM location, bookCopy WHERE bookCopy.bookID = ? AND bookCopy.copyID = ? AND bookCopy.locationID = location.locationID"
        resultLocation = Location.Location()
        self.cursor.execute(query, (bookID, copyID))

        # bookID and copyID are primary keys, so it is impossible to return more than 1 row
        row = self.cursor.fetchall()
        resultLocation.locationID = row[0][0]
        resultLocation.floor = row[0][1]
        resultLocation.section = row[0][2]
        resultLocation.shelfNumber = row[0][3]
        return resultLocation

    def deleteBook(self, bookISBN):
        query = "DELETE FROM book WHERE ISBN = ?"
        self.cursor.execute(query, bookISBN)
        self.database.connectionHead.commit()
        return True

    def deleteUser(self, userEmail):
        query = "DELETE FROM person WHERE email = ?"
        self.cursor.execute(query, userEmail)
        self.database.connectionHead.commit()
        return True

    def getNoOfBooks(self):
        query = "select count(*) from book"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getNoOfStudents(self):
        query = "select count(*) from person where isAdmin = 0"
        cursor = self.database.getCursor()
        cursor.execute(query)
        return cursor.fetchall()

    def getNoOfBooksForEveryGenre(self):
        query = "select  genre, count(*) from bookGenre group by genre order by genre"
        cursor = self.database.getCursor()
        cursor.execute(query)
        return cursor.fetchall()

    def getNoOfBooksForEveryLang(self):
        query = "select  language, count(*) from book group by language order by language"
        cursor = self.database.getCursor()
        cursor.execute(query)
        return cursor.fetchall()

    def addBookGenre(self, ISBN, genre):
        bookID = self.getBooksBy("ISBN",ISBN)[0].BookID
        query = "INSERT INTO bookGenre (bookID, genre) VALUES (?, ?)"
        self.cursor.execute(query, (bookID, genre))
        self.database.connectionHead.commit()

    def addBookCopy(self, ISBN, floor , section , shelfNumber, copyID):
        bookID = self.getBooksBy("ISBN",ISBN)[0].BookID
        #insert to location table
        query = "INSERT INTO location (floor, section, shelfNumber) VALUES (?, ?, ?)"
        self.cursor.execute(query, (floor , section , shelfNumber))
        self.database.connectionHead.commit()
        #get location ID
        locationID = self.getLocationID(floor , section , shelfNumber)[0][0]
        query = "INSERT INTO bookCopy (copyID, bookID, locationID) VALUES (?, ?, ?)"
        self.cursor.execute(query, (copyID, bookID, locationID))
        self.database.connectionHead.commit()

    def getLocationID(self, floor , section , shelfNumber):
        query = "SELECT locationID FROM location WHERE floor = ? AND section = ? AND shelfNumber = ?"
        self.cursor.execute(query, (floor , section , shelfNumber))
        return self.cursor.fetchall()
# you can use DBHead like the following (not real code):

# try:
#     cursor = self.connection.cursor()
#     cursor.execute("SELECT * FROM Books WHERE Title LIKE ?", f'%{title}%')
#     rows = cursor.fetchall()
#     if len(rows) > 0:
#         print("Search results:")
#         for row in rows:
#             print(f"Title: {row.Title}, Author: {row.Author}, Publication Year: {row.PublicationYear}")
#     else:
#         print("No matching books found.")
# except pyodbc.Error as e:
#     print(f"Error searching for book: {str(e)}")
