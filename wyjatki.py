# try except
#napisac funkcje o nazwie div, ktora umozliwi auzytkownikowi podzielenie 2 liczb z precyzja do 2 miejssc po przecinku
'''
def div(x, y):
    try:
        result = x / y
        return result:
        except ZeroDivisionError:
            print('pamietaj')

print(round(div(2,3),2))
print(div(2,0))'''

while True:
   try:
    num = int(input('Podaj liczbe całkowitą: '))
    print(f'Podałeś z klawiatury: {num}')
    break
   except ValueError:
    print('Podana wartośc z klawiatury nie jest liczbą całkowitą\n')
