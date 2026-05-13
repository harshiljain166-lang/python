#Count Vowels from given string
# a="sheriyians"
# count=0
# for i in a:
#     if i in "aeiouAEIOU":
#         count+=1
# print(count)


#36) Reverse a string
# a="sheriyians"
# s= " "
# for i in range(len(a)-1,-1,-1):
#     s+=a[i]
# print(s)


#check wheather two strings are anagram
# a="nana"
# c="naan"
# if len(a)!=len(c):
#     print("not a anagram")
# elif sorted(a)==sorted(c):
#     print("anagram")
# else:
#     print("not an anagram")




#EXTRACT only even index string


# a="harshil"
# # print(a[::2])

# s=""
# for i in range (0,len(a),2):
#     # if i%2==0:
#     s+=a[i]
# print(s)






#REMOVE DUPLICATE CHARACTER FROM A STRING


# a="banana"
# dic={}
# #count the frequency
# for i in a:
#     if i in dic:
#        dic[i]+=1
#     else:
#         dic[i]=1
# print(dic)
# s="" 
# for i in dic:
#     if dic[i]==1:
#         s+=i
# print(s)


#REMOVE DUPLICATE CHARACTER FROM A STRING and keep only 1


# a="banana"
# s=""
# for i in a:
#     if i not in s:
#         s+=i
# print(s)