# class ke andar ka data outsider na dekh sake


#attribute
# 1.public
# 2.private
# 3.protected


# __a="sample".> private
# _a="sample"> protected
# a="sample">public


# class encapsulation:
#     def __init__(self):
#         self.name="this is a public attribute"
#         self._age="this is a protected attribute"
#         self.__year="this is a private attribute"
#     def show(self):
#           print(f"{self.name}")
#           print(f"{self._age}")
#           print(f"{self.__year}")
          



# class sagarGaire:
#     def __init__(self,name):
#         self.name=name
        
#     dish="paneer kulcha"
#     def show(self):
#         print(f"Dish is  {self.dish},{self.name}")

# obj1=sagarGaire('paneer sandwich')
# obj1.show()


#_______________________________________ static method____________________________________________________________


# class sagarGaire:


#     @staticmethod
#     def show():
#         print("aasi tusi")


# obj1=sagarGaire()
# obj1.show()

#_________________________________________________________________________________________________________________________________

# # class sample:
# #     def __init__(self,a1,a2,a3):
# #         self.a1="this is public"
# #         self.__a2="this is private"
# #         self._a3="this is protected"


# #     def show(self):        #getter
# #         print(self.a1)
# #         print(self.__a2)
# #         print(self._a3)
# #     def change(self):      #setter
# #         self.__a2="this is not a public attribute"



# # obj=sample(1,2,3)
# # obj.change()
# # obj.show()
        
# #_____________________________________________________________________________________________________________________________________


# class sharmaVishnu:
#     def __init__(self, dish, price):
#         self.dish = dish
#         self.price = price
#         self.__revenue = 30000  


   
#     @property
#     def show(self):
#         print(f"dish is {self.dish}")
#         print(f"price is {self.price}")
#         print(f"revenue is {self.__revenue}")


#     @show.setter    #getter
#     def change_dish(self,dish):
#         self.__revenue=dish    

# paaji = sharmaVishnu("paneer kulche, 3+kulche", 180)

# paaji.change_dish(50000)
# paaji.show

#__________________________________________________________________________________________________________________________________________
# class bank:
#     def __init__(self,name, age , address):
#         self.name=name
#         self.age=age
#         self.address=address
#         self.__balance=10000000
        

#     @property
#     def show(self):
#         print(f"customer name is {self.name}")
#         print(f"customer age is {self.age}")
#         print(f"customer address is {self.address}")
#         print(f"custome balance  is {self.__balance}")


#     @show.setter
#     def change_balance(self, amount):
#         self.__balance+=amount

# user1=bank("neerav modi",55,"LONDON")
# user1.change_balance=25000000
# user1.show   