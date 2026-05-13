# l=[1,2,2,2,1,3,1,4,5,6,9,5,2]
# d={}
# for i in l:
#     if i not in d :
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)

#   sum of two dictonaries


# d1={"a":10, "b": 20,"c":30}
# d2={"d":10, "a": 5,"c":100}

# for i in d2:
#     if i not in d1:
#         d1[i]=d2[i]
#     else:
#         d1[i]+=d2[i]
# print(d1)




#    SETS
# 1.unorderd
# 2.{}-> comma seprated 
# 3.unique elements store

#s={}
# l=[1,2,2,2,1,3,1,4,5,6,9,5,2]
# s=set(l)
# print(s)


# #2 pop
# s.pop()
# print(s)#first element removed 


# #3 remove 
# s.remove(4)
# print(s)

# #4 intersection
# s1={12,23,34,56,76}
# s2={12,23,34,65,67}
# print("interscection = ",s1.intersection(s2))


# #5 union 
# s1={12,23,34,56,76}
# s2={12,23,34,65,67}
# print("union = ",s1.union(s2))

# #6 difference 
# s1={12,23,34,56,76}
# s2={12,23,34,65,67}
# print("difference  = ",s1.difference(s2))

# #7 symmeteric difference 
# s1={12,23,34,56,76}
# s2={12,23,34,65,67}
# print("symmeteric = ",s1.symmetric_difference(s2))