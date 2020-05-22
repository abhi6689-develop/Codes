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


class Max69:
    def __init__(self,num):
        self.num = num 
    
    def check(self):
        i = 0 
        maximum = 0 
        number = str(self.num)
        while i <= len(number):
            if number[i] == '6':
                number[i] = '9' 
            else:
                number[i] = '6' 
            number = int(number)

            if number >= maximum:
                maximum = number 
            number = str(self.num)
            i += 1 
        return maximum 

max = Max69(9669)
print(max.check())
            
            





           


