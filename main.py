
# import Model.Database as db
from Controller.Controller import Controller
# from Model.Person import Person
# from Model.Authenticator import Authenticator

print("---MAIN---")
print("yabo")
# dummy = db.Database()
mainController = Controller()

if mainController.logIn("admin@example.com", "02829fb05c3076ec5a6caebd12477dec"):
    print("Successful Log In,  WELCOME")
else:
    print("Can't Log In")
# list of student info
studentInfoList = [99, "Ali", "Omar", "1061988605", "2003-06-17", 1, 0, "Ali@example.com", "Alipassword"]
mainController.addStudent(studentInfoList)
# mainController
# mainController



