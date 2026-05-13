# ____________________________________________OOPM________day 1_______________________________________________
# jis class ka object hoga us class ka attribute aur method  call kar paoge


# class Sharmavishnu:
#     a=10#attribute
#     def show(self):
#         print("chole bhature")

#     def display(self):
#         self.name='shan rai'
#         print(f"name is {self.name}")
#     def __init__(self,waiter,chairs,table):
#         self.waiter=waiter#these are instance attributes
#         self.chairs=chairs
#         self.table=table
#         print("constructor function is  called :")
#     def show(self):
#         print(f"waiter name is {self.waiter}")
#         print(f"number of table is {self.table}")
#         print(f"number of chair is {self.chairs}")



# indrapuri=Sharmavishnu('nathulal',20,10)
# indrapuri.show()
# newmarket=Sharmavishnu()
# mp_nagar=Sharmavishnu()






# mp_nagar.display()


# indrapuri.show()
# print(indrapuri.a)

# mp_nagar.show()
# print(mp_nagar.a)

# newmarket.show()
# print(newmarket.a)

#________________________________OOPM day2 _____________________________________________________________________

#________________________________OOPM DAY 3_____________________________________________________________________
#we have to create a class as information  and accept name and age from user and just print name and the age of the user


# class information:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print(f"the name is {self.name} and age is {self.age}")
# obj=information("rama",25)
# obj.show()         
        


#create a class bank as class initialize it must ask the balance of user and if user calls methhod deposite then it  should  ask money to be deposited  and add it to balance than display updated balance
# class bank:
#     def __init__(self,balance):
#         self.balance=balance
#         print=(f"the balance is {self.balance}")
        
#     def deposit(self,amount):
#         self.balance+=amount
#         print(f"the updated amount is {self.balance}")
# obj2=bank(5000)
# obj2.deposit(2000)


#_______________________________________________________________________________________________________


# class student:
#     college="SIRT"
#     @classmethod
#     def change_colllege(cls,new_name):
#         cls.college=new_name
#         print(f"college is {new_name}")
# stdu1=student()
# print(stdu1.college)
# stdu1.change_colllege("LNCT")


#________________________________________________________________________________________________________

# class Sharmavishnu:
#     def __init__(self,waiter):
#         self.waiter = waiter
#     def show(self):
#         print(f"the waiter  name is {self.waiter}")
# indrapuri=Sharmavishnu("raja")
# indrapuri.show()


