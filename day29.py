#   2176. Count Equal and Divisible Pairs in an Array  
# class Solution(object):
#     def countPairs(self, nums, k):
#         count=0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]==nums[j]and(i*j)%k==0:
#                     count+=1
#         return count




#2169. Count Operations to Obtain Zero
# class Solution:
#     def countOperations(self, num1: int, num2: int) -> int:
#         count = 0
#         while num1 != 0 and num2 != 0:
#             if num1 >= num2:
#                 num1 -= num2
#             else:
#                 num2 -= num1
#             count += 1
#         return count



# you  have given a dictionary of items with their price
# dic = {'a':100 ,'b':50 ,'c':200}

