from Controller.Controller import Controller
from View.App import App


mainController = Controller()
mainView = App(mainController)
mainView.mainloop() 

