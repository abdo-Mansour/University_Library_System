
# import Model.Database as db
from Controller.Controller import Controller
from View.App import App
import Model.Library as L
import Model.Book as book
# from Model.Person import Person
# from Model.Authenticator import Authenticator


mainController = Controller()
mainView = App(mainController)
mainView.mainloop() 

