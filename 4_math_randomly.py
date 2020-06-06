#pi
import math
pi=math.pi
print(pi)

#pierwiastek
x=math.sqrt(9)
print((x))
print(type(x))

print(math.floor(2.9999)) #2
print(math.ceil(2.9999)) #3

print(2 ** 10)
print(math.pow(2,10))

#moduł random
import random as r
rand=r.random()
print(rand)

randOfList=r.choice([1, 2, 3, 4])
print(randOfList)

print(r.randrange(10, 20))
print(r.randrange(10))
print(r.randrange(7,13,2))

##########################################

numList = [10, 20, 30, 40, 45]
numTuple = (1, 2, 3, 4, 5, 6)
text = "Janusz"

print("Lista: " + str(r.choice(numList)))
print("Tuple: " + str(r.choice(numTuple)))
print("Text: " + str(r.choice(text)))

###################################

print(numList)
r.shuffle(numList)
print(numList)