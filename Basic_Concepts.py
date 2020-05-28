# word = "Asma"
# print(list(enumerate(word,100)))

# lyst = ['Eat', 'Drink', 'Sleep']
# for index,item in enumerate(lyst):
#     print(index)

x = lambda a: a+10
print(x(5))

x = lambda a,b : a**b
print(x(2,3))

x = lambda a,b,c : a+b+c
print(x(5,6,7))

def myfunction(n):
    return lambda a: a * n 

doubler = myfunction(2)
tripler = myfunction(3)
print(doubler(33))
print(tripler(33))



