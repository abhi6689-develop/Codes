from collections import Counter
from collections import defaultdict
import collections
import math 
import copy 
class Target:
    def __init__(self, nums, index):
        self.nums = nums 
        self.index = index 
    
    def insertion(self):
        target = []
        for i in range(len(self.nums)):
            j = self.index[i]
            target.insert(j,self.nums[i])
        return target 
    


class Balanced_string:
    def __init__(self, sent):
        self.sent = sent 

    def counter(self):
        hashTable = {'R':0, 'L':0}
        count = 0 
        for i in self.sent:
            if i in hashTable:
                hashTable[i] += 1
                if hashTable['R'] == hashTable['L']:
                    print(hashTable)
                    count += 1
                    hashTable = {'R':0, 'L':0}
        return count 
    



class Minimum_time:
    def __init__(self,points):
        self.points = points
    
    def calculate_time(self):
        seconds = 0  
        for i in range(len(self.points)-1):
            j = i+1
            if self.points[i][1] == self.points[j][1]:
                seconds += abs(self.points[i][0]-self.points[j][0])
            else:
                seconds += abs(self.points[i][1]-self.points[j][1])
        return seconds 



class Lowercase:
    def __init__(self, word):
        self.word = word 

    def convert(self):
        str2 = ""
        for i in range(len(self.word)):
            if ord(self.word[i]) in range(65,91):
                asc = ord(self.word[i])
                print(asc)
                asc += 32
                print(asc)
                str2 += chr(asc)
            else:
                str2 += self.word[i]
                
        return str2


class Skyline:
    def __init__(self, grid):
        self.grid = grid 
    
    def maxIncrease(self):
        max_row = []
        max_column = [] 
        maxRow = 0 
        k = 0 
        sum = 0 
        for i in range(len(self.grid)):
            for j in self.grid[i]:
                if j >= maxRow:
                    maxRow = j
            max_row.append(maxRow)
            maxRow = 0

        while k < len(self.grid):
            res = [sub[k] for sub in self.grid]
            max_column.append(max(res))
            k += 1

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                current_val = self.grid[i][j]
                diff = 0 
                self.grid[i][j] = min(max_row[i],max_column[j])
                diff = self.grid[i][j] - current_val
                sum += diff
        return sum


class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
    
class LinkedList:
    def __init__(self):
        self.head = None 
    
    def toDecimal(self):
        string = ""
        sum = 0 
        temp = self.head
        while temp:
            string += str(temp.data)
            temp = temp.next 
        for i in range(len(string)-1, -1, -1):
            decimal = int(string[i])*(2**(len(string)-1-i))
            sum += decimal
        return sum 
    
# lyst = LinkedList()
# lyst.head = Node(1)
# second = Node(0)
# third = Node(1)
# lyst.head.next = second
# second.next = third
# print(lyst.toDecimal())


class Permutation:
    def __init__(self, queries, m):
        self.queries = queries
        self.m = m 
    def process(self):
        i = 0 
        output = []
        p = [i for i in range(1,self.m+1)]
        while i < len (self.queries):
            number = self.queries[i]
            for j in p:
                if j == number:
                    output.append(p.index(j))
                    p.remove(j)
                    p.insert(0,j)
            i += 1 
        return output
                
# permutation = Permutation([7,5,5,8,3], 8)
# print(permutation.process())

class Maximum69:
    def __init__(self, num):
        self.num = num 
    def replace(self):
        strNum = [str(i) for i in str(self.num)]
        max = self.num 
        i = 0 
        new_no = ""
        while i < len(strNum):
            if strNum[i] == '9':
                strNum[i] = '6'
            else:
                strNum[i] = '9'
            for j in strNum:
                new_no += j 
            print(new_no)
            if int(new_no) >= max:
                max = int(new_no)
            strNum = [str(i) for i in str(self.num)]
            new_no = ""
            i += 1


        return max 

# max69 = Maximum69(9999)
# print(max69.replace())


class LuckyNumber:
    def __init__(self, matrix):
        self.matrix = matrix 
    
    def isLucky(self):
        lowest_in_row = float("inf") 
        lows = []
        highs = []
        output = [] 
        for i in self.matrix:
            for j in i:
                if j <= lowest_in_row:
                    lowest_in_row = j
            lows.append(lowest_in_row)
            lowest_in_row = float("inf")

        n = len(self.matrix[0])

        for i in range(n):
            res = [blob[i] for blob in self.matrix]
            highs.append(max(res))

        for i in self.matrix:
            for j in i:
                if j in highs and j in lows:
                    output.append(j)
        return output

    
class Partition:
    def __init__(self, nums,n):
        self.n = n 
        self.nums = nums 
    
    def arrayPartition(self):
        sortNums = sorted(self.nums)
        i = 0 
        j = 0
        sum = 0 
        pairs = []
        output = []
        while i < len(sortNums):
            while j < self.n:
                pairs.append(sortNums[i])
                i += 1
                j += 1 
            output.append(pairs)
            pairs = []
            j = 0  
        for i in output:
            sum += min(i)
            
        return sum
# part = Partition([1,1], 2)   
# print(part.arrayPartition())     

class BuildAStack:
    def __init__(self, target, n):
        self.target = target 
        self.n = n 

    def stack(self):
        output = [] 
        for i in range(1, self.n+1):
            if i > self.target[-1]:
                break
            if i in self.target:
                output.append("Push")
            else:
                output.append("Push")
                output.append("Pop")
        return output
    
# build = BuildAStack([1,2],4)
# print(build.stack())

class Palindrome:
    def __init__(self, num):
        self.num = num 

    def check(self):
        num2 = copy.deepcopy(self.num)
        print(num2)
        sum = 0 
        while self.num:
            x = self.num % 10
            sum += x * (10**int(math.log(self.num, 10)))
            self.num = self.num // 10 
        
        print("Sum:",sum)
        print(type(sum))
        return sum == num2
    

# palin = Palindrome(121)
# print(palin.check())

class KweakestRow:
    def __init__(self, mat, k):
        self.mat = mat 
        self.k = k 
    
    def calculate(self):
        sum = 0
        strengths = []
        output = []
        for i in range(len(self.mat)):
            for j in self.mat[i]:
                if j == 0:
                    break 
                sum += j 
            strengths.append([i,sum])
            sum = 0 

        strengths.sort(key=lambda x: (x[1],x[0]))
        for i in range(self.k):
            output.append(strengths[i][0])
        return output


# kweak = KweakestRow([[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]], 3)

# print(kweak.calculate())

class RelativeSort:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1 
        self.arr2 = arr2 

    def sortIt(self):
        output = [] 
        temp = []
        for i in self.arr2:
            for j in self.arr1:
                if j == i:
                    output.append(j)
        print(output)
        for i in self.arr1:
            if i not in output:
                temp.append(i)
        temp.sort()
        for i in temp:
            output.append(i)
        return output

# relative = RelativeSort([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6])
# print(relative.sortIt())

class MinimumAbsoluteDifference:
    def __init__(self, arr):
        self.arr = arr 

    def findDiff(self):
        dist = 0 
        minDist = float('inf') 
        output = []
        for i in range(len(self.arr)-1):
            for j in range(i+1, len(self.arr)):
                dist = abs(self.arr[i]-self.arr[j])
                if dist <= minDist:
                    minDist = dist
        for i in range(len(self.arr)-1):
            for j in range(i+1, len(self.arr)):
                if abs(self.arr[i]-self.arr[j]) == minDist:
                    output.append([self.arr[i], self.arr[j]])
        for i in output:
            i.sort()
        output.sort(key = lambda x: (x[0],x[1]))
        return output

# minimumdiff = MinimumAbsoluteDifference([1,3,6,10,15])
# print(minimumdiff.findDiff())
            
class FindIndex:
    def __init__(self, nums, target):
        self.nums = nums 
        self.target = target 

    
    def index(self):
        output = []
        for i in range(len(self.nums)):
            if self.nums[i] == self.target:
                output.append(i)
        if len(output) == 0:
            return [-1,-1]
        return output

# findingNemo = FindIndex([5,7,7,8,8,10],6)
# print(findingNemo.index())

class LowestNumber:
    def __init__(self, num, k):
        self.num = num 
        self.k = k 
    
    def makeLowest(self):
        stack = []
        for i in self.num:
            while self.k > 0 and len(stack)>0 and stack[-1] > i:
                self.k -= 1 
                stack.pop()
            stack.append(i)
        if self.k > 0:
            stack = stack[:-self.k]
        return "".join(stack).lstrip("0") or "0"
    
# lowest = LowestNumber("1432219", 3)
# print(lowest.makeLowest())

class ReplaceGreatest:
    def __init__(self, arr):
        self.arr = arr 
    
    def swap(self):
        # for i in range(len(self.arr)):
        #     max = 0 
        #     for j in range(i+1, len(self.arr)):
        #         if self.arr[j] > max:
        #             max = self.arr[j]
        #     self.arr[i] = max 
        # self.arr[-1] = -1
        # return self.arr 
        i = 0 
        j = len(self.arr)-1 
        while i < j:
            max = 0 
            if self.arr[j] > max:
                max = self.arr[j]
            
    

# replace = ReplaceGreatest([17,18,5,4,6,1])
# print(replace.swap())
            

class SortByPower:
    def __init__(self,lo,hi,k):
        self.lo = lo
        self.hi = hi 
        self.k = k 

    def sorting(self):
        output = []
        count = 0 
        for i in range(self.lo, self.hi+1):
            i2 = i
            while i > 1:
                if i % 2 == 0:
                    i = i/2
                else:
                    i = (3 * i) + 1 
                count += 1
            output.append([i2, count])
            count = 0 

        output = sorted(output, key=lambda x: (x[1],x[0]))
        print(output)
        return output[self.k-1][0]
    
# sortbypower = SortByPower(7,11,4)
# print(sortbypower.sorting())


class AttackKing:
    def __init__(self, queens, king):
        self.queens = queens
        self.king = king 
    
    def Attack(self):
        output = []
        self.queens.sort(key = lambda x: (x[0], x[1]))
        diagonalChecked = False
        rowChecked = False 
        ColumnChecked = False 
        print(self.queens)
        for i in self.queens:
            if i == self.king:
                continue
            elif self.checkingRow(x = i) == True and rowChecked == False:
                output.append(i)
                rowChecked = True
            elif self.checkingColumn(x = i) == True and ColumnChecked == False:
                output.append(i)
                ColumnChecked = True
            elif self.checkingDiagonal(x = i) == True and diagonalChecked == False:
                output.append(i)
                diagonalChecked = True
        return output

    def checkingRow(self,x):
        y = self.king
        if x[0] == y[0]:
            return True
        return False


    def checkingColumn(self,x):
        y = self.king
        if x[1] == y[1]:
            return True
        return False

    def checkingDiagonal(self,x):
        y = self.king
        if x[1]-y[1] == 0:
            return False
        elif abs((x[0]-y[0])/(x[1]-y[1])) == 1:
            return True
        return False    



        
# attackKing = AttackKing([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]],[3,3])
# print(attackKing.Attack())


class Recurring:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def convert(self):
        output = str(self.numerator/self.denominator)
        print(output)
        string = ""
        for i in range(len(output)):
            if output[i-1] == output[i]:
                string += "("+output[i]+")"
                break
            string += output[i]

        return string
    
# recur = Recurring(2,3)
# print(recur.convert())
    
class UniqueDigits:
    def __init__(self, n):
        self.n = n 
    
    def count(self):
        output = []
        count = 0 
        for i in range(0, (10**self.n)+1):
            if i % 11 == 0:
                pass 
            else:
                output.append(i)
                count += 1 
        print(count)
        return output
   
    
# un = UniqueDigits(2)
# print(un.count())
            
class Superpow:
    def __init__(self, a, b):
        self.a = a 
        self.b = b 

    def up(self):
        num = ""
        B = map(str,self.b)
        for i in B:
            num += i
        return num 
    
# super = Superpow(78267,
# [1,7,7,4,3,1,7,0,1,4,4,9,2,8,5,0,0,9,3,1,2,5,9,6,0,9,9,0,9,6,0,5,3,7,9,8,8,9,8,2,5,4,1,9,3,8,0,5,9,5,6,1,1,8,9,3,7,8,5,8,5,5,3,0,4,3,1,5,4,1,7,9,6,8,8,9,8,0,6,7,8,3,1,1,1,0,6,8,1,1,6,6,9,1,8,5,6,9,0,0,1,7,1,7,7,2,8,5,4,4,5,2,9,6,5,0,8,1,0,9,5,8,7,6,0,6,1,8,7,2,9,8,1,0,7,9,4,7,6,9,2,3,1,3,9,9,6,8,0,8,9,7,7,7,3,9,5,5,7,4,9,8,3,0,1,2,1,5,0,8,4,4,3,8,9,3,7,5,3,9,4,4,9,3,3,2,4,8,9,3,3,8,2,8,1,3,2,2,8,4,2,5,0,6,3,0,9,0,5,4,1,1,8,0,4,2,5,8,2,4,2,7,5,4,7,6,9,0,8,9,6,1,4,7,7,9,7,8,1,4,4,3,6,4,5,2,6,0,1,1,5,3,8,0,9,8,8,0,0,6,1,6,9,6,5,8,7,4,8,9,9,2,4,7,7,9,9,5,2,2,6,9,7,7,9,8,5,9,8,5,5,0,3,5,8,9,5,7,3,4,6,4,6,2,3,5,2,3,1,4,5,9,3,3,6,4,1,3,3,2,0,0,4,4,7,2,3,3,9,8,7,8,5,5,0,8,3,4,1,4,0,9,5,5,4,4,9,7,7,4,1,8,7,5,2,4,9,7,9,1,7,8,9,2,4,1,1,7,6,4,3,6,5,0,2,1,4,3,9,2,0,0,2,9,8,4,5,7,3,5,8,2,3,9,5,9,1,8,8,9,2,3,7,0,4,1,1,8,7,0,2,7,3,4,6,1,0,3,8,5,8,9,8,4,8,3,5,1,1,4,2,5,9,0,5,3,1,7,4,8,9,6,7,2,3,5,5,3,9,6,9,9,5,7,3,5,2,9,9,5,5,1,0,6,3,8,0,5,5,6,5,6,4,5,1,7,0,6,3,9,4,4,9,1,3,4,7,7,5,8,2,0,9,2,7,3,0,9,0,7,7,7,4,1,2,5,1,3,3,6,4,8,2,5,9,5,0,8,2,5,6,4,8,8,8,7,3,1,8,5,0,5,2,4,8,5,1,1,0,7,9,6,5,1,2,6,6,4,7,0,9,5,6,9,3,7,8,8,8,6,5,8,3,8,5,4,5,8,5,7,5,7,3,2,8,7,1,7,1,8,7,3,3,6,2,9,3,3,9,3,1,5,1,5,5,8,1,2,7,8,9,2,5,4,5,4,2,6,1,3,6,0,6,9,6,1,0,1,4,0,4,5,5,8,2,2,6,3,4,3,4,3,8,9,7,5,5,9,1,8,5,9,9,1,8,7,2,1,1,8,1,5,6,8,5,8,0,2,4,4,7,8,9,5,9,8,0,5,0,3,5,5,2,6,8,3,4,1,4,7,1,7,2,7,5,8,8,7,2,2,3,9,2,2,7,3,2,9,0,2,3,6,9,7,2,8,0,8,1,6,5,2,3,0,2,0,0,0,9,2,2,2,3,6,6,0,9,1,0,0,3,5,8,3,2,0,3,5,1,4,1,6,8,7,6,0,9,8,0,1,0,4,5,6,0,2,8,2,5,0,2,8,5,2,3,0,2,6,7,3,0,0,2,1,9,0,1,9,9,2,0,1,6,7,7,9,9,6,1,4,8,5,5,6,7,0,6,1,7,3,5,9,3,9,0,5,9,2,4,8,6,6,2,2,3,9,3,5,7,4,1,6,9,8,2,6,9,0,0,8,5,7,7,0,6,0,5,7,4,9,6,0,7,8,4,3,9,8,8,7,4,1,5,6,0,9,4,1,9,4,9,4,1,8,6,7,8,2,5,2,3,3,4,3,3,1,6,4,1,6,1,5,7,8,1,9,7,6,0,8,0,1,4,4,0,1,1,8,3,8,3,8,3,9,1,6,0,7,1,3,3,4,9,3,5,2,4,2,0,7,3,3,8,7,7,8,8,0,9,3,1,2,2,4,3,3,3,6,1,6,9,6,2,0,1,7,5,6,2,5,3,5,0,3,2,7,2,3,0,3,6,1,7,8,7,0,4,0,6,7,6,6,3,9,8,5,8,3,3,0,9,6,7,1,9,2,1,3,5,1,6,3,4,3,4,1,6,8,4,2,5])
# print(super.up())

class Maxproduct:
    def __init__(self, nums):
        self.nums = nums 
    
    def calculate(self):
        max = 0 
        for i in range(len(self.nums)):
            for j in range(len(self.nums)):
                if i != j:
                    product = (self.nums[i]-1) * (self.nums[j]-1)
                    if product > max:
                        max = product
        return max 
    
# maxproduct = Maxproduct([3,4,5,2])
# print(maxproduct.calculate())

class LuckyNumber2:
    def __init__(self, arr):
        self.arr = arr
    def check(self):
        dict = {}
        max = -1 
        for i in self.arr:
            if i not in dict:
                dict[i] = 1 
            else:
                dict[i] += 1 
        for i, j in dict.items():
            if i == j and i > max:
                max = i 


        return max
 
    
# lucky = LuckyNumber2([1,2,2,3,3,3])
# print(lucky.check())

class Complement:
    def __init__(self, num):
        self.num = num 
    
    def revert(self):
        binaryStr = ""
        complement = ""
        sum = 0 
        while self.num:
            binaryStr += str(self.num % 2)
            self.num = self.num//2 
        for i in binaryStr[::-1]:
            if i == "1":
                complement += "0"
            else:
                complement += "1"
        print(binaryStr[::-1])
        complement = complement[::-1]
        for i in range(len(complement)):
            sum += int(complement[i]) * 2**i
        return sum 

            

class MakeTarget:
    def __init__(self, target, arr):
        self.target = target
        self.arr = arr
    def reverse(self):
        print(Counter(self.target))
        print(Counter(self.arr))
        return Counter(self.target)==Counter(self.arr)

# maketarget = MakeTarget([1,2,3,4],[2,4,1,3])
# print(maketarget.reverse())


class SearchResult:
    def __init__(self, products, searchWord):
        self.products = products
        self.searchWord = searchWord
    
    def search(self):
        self.products.sort()
        searchString = ""
        output = []
        i = 0 
        while len(searchString) < len(self.searchWord):
            searchString += self.searchWord[i]
            print(searchString)
            results = []
            for j in self.products:
                if j.startswith(searchString) and len(results) < 3:
                    results.append(j)
            output.append(results)
            i += 1
        return output
        
# amazon = SearchResult(["mobile","mouse","moneypot","monitor","mousepad"], "mouse")
# print(amazon.search())

class SortByFrequncy:
    def __init__(self, s):
        self.s = s 
    
    def sort(self):
        output = ""
        dictionary = Counter(self.s)
        dictionary = sorted(dictionary.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
        for i in dictionary:
            output += i[0]*i[1]
        print(output)

# sortbyfrequency = SortByFrequncy("cccaaa")
# sortbyfrequency.sort()

class KPlacesAway:
    def __init__(self, nums, k):
        self.nums = nums 
        self.k = k 
    
    def check(self):
        kDistance = [] 
        count = 0 
        foundOne = False
        for i in range(len(self.nums)-1):
            if self.nums[i] == 1 and foundOne == False:
                foundOne = True
                count = 0
            count += 1 
            i += 1
            if self.nums[i] == 1 and foundOne == True:
                foundOne = False
                kDistance.append(count-1)
        for i in kDistance:
            if i < self.k:
                return False
        return True
  
# kplaces = KPlacesAway([1,1,1,1,1], 0)
# print(kplaces.check())

                
class greaterLetter:
    def __init__(self, letters, target):
        self.letters = letters 
        self.target = target 
    
    def find(self):
        smallest = float("inf")
        for i in self.letters:
            if ord(i) < ord(self.target):
                continue
            elif ord(i) > ord(self.target) and ord(i) < smallest:
                smallest = ord(i)
            
        if ord(self.target) >= ord(self.letters[-1]):
            return self.letters[0]
        else:
            return chr(smallest)
    
greaterlet = greaterLetter(["c", "f", "j"], "k")
print(greaterlet.find())

class TopKfrequent:
    def __init__(self, words, k):
        self.words = words 
        self.k = k 
    
    def findfreq(self):
        hash_table = Counter(self.words)
        hash_table = sorted(hash_table.keys(), key = lambda x: (-hash_table[x], x))
        print(hash_table)
        return hash_table[:self.k]
       
    

topk = TopKfrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
print(topk.findfreq())




           




           


