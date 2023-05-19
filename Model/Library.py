import Database as db

class Library:
    def __init__(self):
        DBHead = db.Database.connectToDataBase() # This is used as the curser for the database
        pass

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


