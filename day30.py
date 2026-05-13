#2164 leet code : Sort Even and Odd Indices Independently
# even = []
#         odd = []

#         # Step 1: Separate
#         for i in range(len(nums)):
#             if i % 2 == 0:
#                 even.append(nums[i])
#             else:
#                  odd.append(nums[i])
# Step 2: Sort
#         even.sort()
#         odd.sort(reverse=True)

#         # Step 3: Merge back
#         e = o = 0
#         for i in range(len(nums)):
#             if i % 2 == 0:
#                 nums[i] = even[e]
#                 e += 1
#             else:
#                 nums[i] = odd[o]
#                 o += 1




# 2160. Minimum Sum of Four Digit Number After Splitting Digits
# num=2932
# a=list(str(num))
# a.sort()
# n1=int(a[0])*10+int(a[-1])
# n2=int(a[0])*10+int(a[-2])
# print(n1,n2)