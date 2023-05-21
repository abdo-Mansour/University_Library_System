
class Person:
    def __init__(self, id=None, firstName=None, lastName=None, number=None, dob=None, sex=None, isAdmin=None, email=None, password=None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.number = number
        self.dob = dob
        self.sex = sex
        self.isAdmin = isAdmin
        self.email = email
        self.password = password

    def printPersonInfo(self):
        print("id: ",self.id)
        print("Fname: ",self.firstName)
        print("Lname: ",self.lastName)
        print("phone: ",self.number)
        print("dob: ",self.dob)
        print("sex: ",self.sex)
        print("isAdmin: ",self.isAdmin)
        print("email: ",self.email)
        print("password: ",self.password)
