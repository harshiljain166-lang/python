# def sample(param):   #function define
#     print("hello world")
# sample("paaji")#function call

#syntax:
# lambda PARAMETERS: CODE TO BE EXECUTED IF PARAMETER ARE THERE.
#lambda  -> keyword


#adds up two numbers :
# sum = lambda a,b:a+b
# print(sum(10,10))

#accept a numbers as parameter and check the number is even or odd:
# n=lambda x:"even"if x%2 ==0 else "odd"
# print(n(9))

# index=lambda l,i=0:l[i]
# print(index(2,[10,20,30,40]))

#keyword parameters or keyword arrguments
# jab ha funtion define karte hai

# sample=lambda name,gender,age:print(name ,gender ,age)
# sample(name="raja", gender="Male",age="12")



     
                                               ###leetcode##################




# 2357. Make Array Zero by Subtracting Equal Amounts
#stages 
# we have to create a empty set
#nums ke saare elements set mai pass karna hai but 0 ni
# s=set()
#         for i in nums:
#             if i !=0:
#                 s.add(i)
#         return len(s) 