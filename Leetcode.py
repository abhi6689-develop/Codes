from collections import Counter
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
    
lyst = LinkedList()
lyst.head = Node(1)
second = Node(0)
third = Node(1)
lyst.head.next = second
second.next = third
print(lyst.toDecimal())


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
                
permutation = Permutation([7,5,5,8,3], 8)
print(permutation.process())

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

max69 = Maximum69(9999)
print(max69.replace())

print(1%2)










            
            
            
            

        


            
            





           


