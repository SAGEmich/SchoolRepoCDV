#listy
progr=['PHP', 'Python']
print(type(progr))
progr.append('C#')
print(progr)
count=progr.count('PHP')
print(f'PHP występuje {count} razy\n')

#tuple
name=('Krystyna', 'Anna')
print(name)
print(type(name))
first=name[0]
print(first)
#name.append('Janusz')
print()

#słowniki

person = {
  'name':'Anna',
  'surname':'Nowak'
}

print(person)
print(type(person))
print(person['name'])
print(person.keys())
print(person.get('height', 'brak danych'))

person['height']=178
print(person.get('height', 'brak danych'))

print()

'''
Utwórz słownik i przypisz mu trzy imiona podane z klawiatury
wyświetl te dane na ekranie w formacie:
Imię1: ...
Imię2: ...
Imię3: ...
'''

n1 = input("\nPodaj pierwsze imię:")
n2 = input("Podaj drugie imię:")
n3 = input("Podaj trzecie imię:")

name = {
  0:n1,
  1:n2,
  2:n3
}

for key, value in name.items():
  count=key+1
  print(f'Imię{count}:{value}')

'''
print(f'Imię1: {name[0]}')
print(f'Imię2: {name[1]}')
print(f'Imię3: {name[2]}')
'''
