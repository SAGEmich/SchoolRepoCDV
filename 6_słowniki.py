worker = {
    'name': 'Michal',
    'nazwisko': 'Znaj', 
    'wiek': 21, 
    'dzieci': ['Jas' , 'Zosia'], 
    'rodzice': ['Anna' , 'Robert']
    }

print(worker)
print(worker['dzieci'])
print ('Dziecko 1: ' + str(worker["dzieci"][0]))
print ('Dziecko 2: ' + str(worker["dzieci"][1]))

worker['height'] = 180
worker['weight'] = 80

print(worker)

key='age'

if key in worker:
    del worker[key]
    print(f'Klucz o nazwie {key} został usunięty')

else:
        
        print(f'Klucz o nazwie {key} nie został znaleziony w słowniku')

        print(worker)

print(worker)

for key, value in worker.items():
    print(f'{key}:{value}')