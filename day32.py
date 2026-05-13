#31) Print string in reverse,its length,in uppercase,lowercase and copy into another string
#  0 to 5
# s="chacha"
# print(len(s))
# print(s.upper())
# print(s.lower())
# a=s
# print(a)

#32) Arrange string characters such that lowercase letters should come first

# a="hArsHiL"
# b=""
# c=""
# for i in a:
#     if i.islower():
#         b+=i
#     else:
#         c+=i
# print(b+c)

#33) Count all letters, digits, and special symbols from a given string
    # Given: str1 = "P@#yn26at^&i5ve"


# str="P@#yn26at^&i5ve"
# char=0 
# digit=0
# symbol=0
# for i in str:
#     if i.isalpha():
#         char+=1
#     elif i.isdigit():
#         digit+=1
#     else:
#         symbol+=1
# print("char:",char)
# print("digit:",digit)
# print("symbol:",symbol)


#34) Compare two strings without using inbuilt functionsx


# a="s"
# b="s"
# if len(a)!=len(b):
#     print("not equal")
# else:
#     for i in range(len(a)):
#         if a [i]!=b[i]:
#             print("not equal")
#             break
#     else:
#         print("equal")