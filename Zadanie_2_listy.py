country = ["Polska", "Niemcy", "Francja", "Szkocja", "USA"]
country.append(input("Podaj jeden kraj: "))
country.append(input("Podaj drugi kraj: "))
a=input("""wpisz liczbę dla opcji którą podasz potem kliknij enter:
1) Wyświetl trzy pierwsze elementy z listy
2) Wyświetl elementy które dodałeś
3) Wyświetl zawartość z listy
4) Wyczyść zawartość
5) Znajdź elementy w liście, które podasz
""")

if a=='1':
    print(country[0:3])
elif a=='2':
    print(country[4:2])
elif a=='3':
    print(country)
elif a=='4':
    country.clear()
elif a=='5':
    g=input("Podaj szukany element: ")
    if g>0:
        print("Jest")
    else:
        print("Nie ma")
else:
    print("Zła komenda")
print(country)