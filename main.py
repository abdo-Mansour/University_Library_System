
# import Model.Database as db
from Controller.Controller import Controller
import Model.Library as L
import Model.Book as book
# from Model.Person import Person
# from Model.Authenticator import Authenticator

print("---MAIN---")
print("yabo")
# dummy = db.Database()
# mainController = Controller()
# mainController
f = L.Library()
b = book.Book()
data = ['The Great Gatsby', 5218, '11', 'English',
        'A novel by F. Scott Fitzgerald', 'Scribner', 14, 1925]
attrs = ['Title', 'PageCount', 'ISBN', 'Language', 'Description',
         'Publisher', 'MinimumAgeToRead', 'PublicationYear']
for attribute_name, val in zip(attrs, data):
    setattr(b, attribute_name, val)

f.addBook(b)
