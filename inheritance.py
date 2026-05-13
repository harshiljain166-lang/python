#___________________________________________________________INHERITANCE_________________________________________________________-

# single level
# multiple
# multilevel
# hierarichial
# hybrid

#______________________________________________________________________________________________________________________________-

# class animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print(f"Name is {self.name} and age is {self.age} ")
# class cat(animal):
#     def show2(self):
#         print("this is cat class")
# obj=cat("rockey",5)
# obj.show()
# obj.show2()

#__________________________________________________________________________________________________________________________________

# class Animal:
#     def __init__(self, name, age, gender="male"):
#         self.name = name
#         self.age = age
#         self.can_walk = True
#         self.gender = gender

#     def show(self):
#         print(f"Name: {self.name}, Age: {self.age}, Can walk: {self.can_walk}")

#     def sleep(self):
#         self.can_walk = False

#     def show_gender(self):
#         print(f"Gender of my animal is {self.gender}")


# class Cat(Animal):
#     def __init__(self, name, age, breed, gender="male"):
#         super().__init__(name, age, gender)
#         self.breed = breed

#     def show2(self):
#         print(f"This is a cat: {self.name}, {self.age}, {self.breed}")


# obj = Cat("tom", 5, "persian")
# obj.sleep()
# obj.show()
# obj.show2()
# obj.show_gender()
#________________________________________________________________________________________________________________


#MULTILEVEL INHERITANCE


# class a:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print("this is parent class")

# class b(a):
#     def __init__(self, name,weight):
#         super().__init__(name)
#         self.weight=weight


#     def show2(self):
#         print("this is a child" )

# class c(b):
#     def __init__(self, name,age, weight,gender):
#         super().__init__(name,weight)
        
#         self.age=age
#         self.gender=gender
    
#     def show3(self):
#         print(f"{self.name},{self.age},{self.gender},{self.weight}")


# obj=c("chacha",56,"M" ,65)
# # obj.show()
# # obj.show2()
# obj.show3()       

# ______________________________________________________________________________________________________________________



# class a:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print("this is parent class")


# class b(a):
#     def __init__(self, name, weight):
#         super().__init__(name)
#         self.weight = weight

#     def show2(self):
#         print("this is a child")


# class c(b):
#     def __init__(self, name, age, weight, gender):
#         super().__init__(name, weight)   
#         self.age = age
#         self.gender = gender

#     def show3(self):
#         print(f"{self.name}, {self.age}, {self.gender}, {self.weight}")


# obj = c("chacha", 56, 65, "M")
# obj.show3()



#________________________________________________________________________________________________________________
#                                multiple inheritance

# class restaurant:
#     def __init__(self):
#         print("this is restaurent class(parent 1)")
# class menu:
#     def __init__(self):
#         print("this ia menue class (parent 2)")
# class customer(restaurant,menu):
#     pass

# obj=customer()

#_________________________________________________________________________________________________________________________________________


# class bank:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"this is a bank class  {self.name}")
# class account:
#     def __init__(self,account_no):
#         self.account_no=account_no
#     def show2(self):
#         print(f"this is a account class{self.account_no}")

# class customer(bank,account):
#     def __init__(self, name,account_no):
#         account.__init__(self,account_no)
#         bank.__init__(self,name)
#     def show3(self):
#         print("this is customer class")



# obj=customer("vijay","124536")
# obj.show()
# obj.show2()
# obj.show3()
#___________________________________________________________________________________________________________________

#      HYBRID INHERITANCE

# class papa:
#     def skill(self):
#         print("belt hee belt")

# class mother:
#     def skill(self):
#         print("taana dena")

# class child(papa):#single
#     def skill(self):
#         print("na hai na hogi")

# class student(child):#multilevel
#     def skill(self):
#         print("chit banana")    

#__________________________________________________________________________________________________________________
# class A:
#     def show(self):
#         print("this is a class")
# class B(A):
#     pass

# class C(A):
#     pass
#________________________________________________________________________________________________________________
