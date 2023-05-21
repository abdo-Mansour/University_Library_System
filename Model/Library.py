import Model.Database as db
import Model.Book as Book


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
        query = "SELECT * FROM Book WHERE "
        query += column + ' = ?'
        self.cursor.execute(query, value)
        return self.bookDataParse()

    def getNBooks(self, N, offset):
        query = "SELECT * FROM book ORDER BY bookID OFFSET ? ROWS FETCH NEXT ? ROWS ONLY;"
        self.cursor.execute(query, (offset, N))
        return self.bookDataParse()

    def addBook(self, book):
        attributes = ['Title', 'PageCount', 'ISBN', 'Language',
                      'Description', 'Publisher', 'MinimumAgeToRead', 'PublicationYear']
        query = "INSERT INTO book ("
        for i in range(len(attributes)):
            query += attributes[i]
            if i < len(attributes)-1:
                query += ', '
            else:
                query += ')'
        query += "VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)"
        valuesList = []
        for i in range(len(attributes)):
            valuesList.append(getattr(book, attributes[i]))
        self.cursor.execute(query, tuple(valuesList))

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
