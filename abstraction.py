# abstraction hamesha inheritance ke sath hoga 
#   A B C
# abstract base class
# abstract method
# data abstraction python me direct use ni kar sakte
#___________________________________________________________
from abc import ABC,abstractmethod

class sharma_vishnu(ABC):
    def greet(self):
        print("welcome to sharma vishnu ")

    @abstractmethod
    def menu(self):
        pass
    
    @abstractmethod
    def details(self):
        pass


class minal(sharma_vishnu):
    def show(self):
        print("this is minal class ")

    def menu(self):
        print("cheese sandwich  , paneer kucha ")

    def details(self):
        print("details ......")

obj=minal()
obj.details()
obj.greet()
obj.menu()
obj.show()

#_____________________________________________________________________________________________________
# from abc import ABC,abstractmethod

# class BankApp(ABC):
#     def database(self):
#         print("data base  create  and accessed")

#     @abstractmethod
#     def account(self):
#         pass

# class webapp(BankApp):
#     def account (self):
#         print("account accessed")


# class mobApp(BankApp):
#     def account(self):
#         print("this is account of mobile class")


# obj=webapp()
# obj.database()
# obj.account()
