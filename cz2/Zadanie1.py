from random import randint

a = -3.22
b = 2.91

# zapytanie uzytkownika
while True:
    while True:
        try:
            dol = int(input('Podaj dolna wartosc zakresu dla możliwego c: '))
            break
        except:
            continue
    while True:
        try:
            gora = int(input('Podaj gorna wartosc zakresu dla możliwego c: '))
            break
        except:
            continue
    if dol < gora:
        break


c = randint(dol, gora)

# stworzenie listy y
ylist = []
xlist = []
# range okresla przedzial od -20 do 25 po prawej nawias otwarty
# 5 to skok
for i in range(-20, 25, 5):
    xlist.append(i)
    ylist.append(a*(i**2)+(b*i)+c)

# wyswietlenie wynikow
x = 0
for i in ylist:
    print(f'\nx: {xlist[x]}\ny: {i}')
    x += 1
