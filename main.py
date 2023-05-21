
# import Model.Database as db
from Controller.Controller import Controller
import Model.Library as L
import Model.Book as book
# from Model.Person import Person
# from Model.Authenticator import Authenticator


mainController = Controller()

if mainController.logIn("admin@example.com", "02829fb05c3076ec5a6caebd12477dec"):
    print("Successful Log In,  WELCOME")
else:
    print("Can't Log In")
# list of student info
studentInfoList = [99, "Abdelrhman", "Amer", "01061988605", "2003-06-17", 1, 0, "abdelrhmanamerali@gmail.com", "Abdelrhmanpassword"]
mainController.addStudent(studentInfoList)

# f = L.Library()
# b = book.Book()
# data = ['The Great Gatsby', 5218, '11', 'English',
#         'A novel by F. Scott Fitzgerald', 'Scribner', 14, 1925]
# attrs = ['Title', 'PageCount', 'ISBN', 'Language', 'Description',
#          'Publisher', 'MinimumAgeToRead', 'PublicationYear']
# for attribute_name, val in zip(attrs, data):
#     setattr(b, attribute_name, val)

# f.addBook(b)
