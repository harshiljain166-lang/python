#  LEET code
# 2210
# class Solution(object):
#     def countHillValley(self, nums):
#         # Remove consecutive duplicates
#         l = [nums[0]]
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 l.append(nums[i])

#         count = 0
#         # Traverse from 1 to len(l)-2
#         for i in range(1, len(l) - 1):
#             if l[i] > l[i + 1] and l[i] > l[i - 1]:
#                 # hill
#                 count += 1
#             elif l[i] < l[i + 1] and l[i] < l[i - 1]:
#                 # valley
#                 count += 1

#         return count


#2154


