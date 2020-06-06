'''#zadanie

n1 = input("\nPodaj pierwsze imie:")
n2 = input("\nPodaj drugie imie:")
n3 = input("\nPodaj trzecie imie:")

name = {
    0:n1,
    1:n2,
    2:n3
}

for key, value in name.items():
count = key + 1
print(f'Imie{count}: {value}')'''