def wyznacz_pierwsze(liczba):
    pierwsze = [2]

    def czy_pierwsza(liczba):
        for dzielnik in pierwsze:
            if liczba % dzielnik == 0:
                return False
            if dzielnik * dzielnik > liczba:
                return True
        return True

    for i in range(2, liczba):
        if czy_pierwsza(i) is True:
            pierwsze.append(i)
    return pierwsze

print(wyznacz_pierwsze(300))

'''input("1 liczba: ")
input("2 liczba: ")
 
def fermat(k, p):
i = 0
 
while i < k:
a = random.randint(1, p - 1)
if pow(a, (p - 1), p) == 1:
i = i + 1
else:
return False
 
return True'''