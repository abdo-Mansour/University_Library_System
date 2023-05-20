import Database as db

class Authenticator:
    def __init__(self, email, password):
        DBHead = db.Database.connectToDataBase() # This is used as the curser for the database
        # if something:
        #    return True
        #   returnPersonData()
        # else
        #    return false

# Make a function here that returns the data of the student if the email and password are correct
    def returnPersonData():
        pass

# you can use DBHead like the following

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


