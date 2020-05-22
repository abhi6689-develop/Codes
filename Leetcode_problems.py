# class Solution:
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right 

#     def isDiv(self,num):
#         if num%10 == 0:
#             return False
#         else:
#             for i in str(num):
#                 if num%int(i) != 0:
#                     return False 
#         return True 
    
#     def checkNum(self):
#         lyst = []
#         for i in range(self.left, self.right+1):
#             if self.isDiv(i):
#                 lyst.append(i)
#         return lyst


# s = Solution(1,22)
# print(s.checkNum())


# class Solution2:
#     def __init__(self, prices):
#         self.prices = prices 

#     def max_profit(self):
#         if self.prices == []:
#             return 0 
#         else:
#             minimium = self.prices[0]
#             for i in self.prices:
#                 if i < minimium:
#                     minimium = i 
#             minimum_index = self.prices.index(minimium)
#             if self.prices[minimum_index] == self.prices[-1]:
#                 return 0 
#             else:
#                 maximum = self.prices[minimum_index+1]
#                 for i in range(minimum_index+1, len(self.prices)):
#                     if self.prices[i] > maximum:
#                         maximum = self.prices[i]
#                 if minimum_index < self.prices.index(maximum):
#                     return maximum-minimium
#                 else:
#                     return 0 



# so = Solution2([2,4,1])
# print(so.max_profit())

# class Solution:
#     def __init__(self, height):
#         self.height = height 
#     def water(self):
#         start = 0
#         end = len(self.height)-1 
#         max_area = 0
#         area = 0 
#         while start < end:
#             area = min(self.height[start], self.height[end])*abs(end-start)
#             if area >= max_area:
#                 max_area = area
#             if self.height[start] < self.height[end]:
#                 start += 1
#             else:
#                 end -= 1 
#         return max_area

# solution = Solution([1,8,6,2,5,4,8,3,7])
# print(solution.water())

# class No_of_occurences:
#     def __init__(self, arr):
#         self.arr = arr 
    
#     def get_occurences(self):
#         hashTable = {}
#         stack = []
#         for i in self.arr:
#             if i not in hashTable:
#                 hashTable[i] = 1
#             else:
#                 hashTable[i] += 1 

#         for i in hashTable.values():
#             if i in stack:
#                 return False 
#             stack.append(i)
#         return True

        

# number = No_of_occurences([1,2])
# print(number.get_occurences())

class Target:
    def __init__(self, nums, index):
        self.nums = nums 
        self.index = index 

    def insert(self):
        target = []
        for i in range(len(nums)-1):
            for j in range(0,1):
                
