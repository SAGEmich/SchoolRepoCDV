progr = ['Python', 'C#', 'JS', 'PHP', 'Java']

print(progr)
print(type(progr)) 

first=progr[0]
print(first)

threeElements=progr[0:3]
print(threeElements)

last=progr[-1]
print(last)

secondToLastItem=progr[-2]
print(secondToLastItem)

#dodanie nowego elementu na koniec listy 
progr.append('R')
progr.append('Python')
print(progr)

#zliczanie elementu w liście
countElement=progr.count('Python')
print("Ilość elementów: " + str(countElement))

#Ilość elementów w liście
countElementsOfList=(len(progr))
print(countElementsOfList)

#połączenie list
anotherList=['C', "C++"]
progr.extend(anotherList)
print('Lista progr: ' + str(progr))
print('Lista anotherList: ' + str(anotherList))

#usuwanie elementów z listy
new=progr
print('Lista new: ' + str(new))
new.clear()
print('Lista new: ' + str(new))
print('Rozmiar listy new: ' + str(len(new)))

print('Lista progr: ' + str(progr))
print('Rozmiar listy progr: ' + str(len(progr)))

x=8
print(x)
y=x
print(y)

y=5
print(x)
print(y)