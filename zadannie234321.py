def slownik():
    marka = input("Podaj marke: ")
    model = input("podaj model: ")
    pojemnosc = input("podaj pojemnosc: ")
    pMax = input("Podaj pMax: ")

    samochod = {
        'Marka: ':marka,
        'Model: ':model,
        'Pojemnosc: ':pojemnosc,
        'pMax: ':pMax 
    }
    return samochod

def dane():
        print(slownik())
        dane()

