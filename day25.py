#leet code  day 2

# maximum number of pairs in array

# class Solution(object):
#     def numberOfPairs(self, nums):
#         d = {}

#         # Count frequency of each number
#         for i in nums:
#             if i not in d:
#                 d[i] = 1
#             else:
#                 d[i] += 1

#         pairs = 0
#         leftovers = 0

#         # Calculate pairs and leftovers
#         for j in d.values():
#             pairs += j // 2
#             leftovers += j % 2

#         return [pairs, leftovers]
