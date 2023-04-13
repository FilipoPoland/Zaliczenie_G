# Zapytaj uzytkownika odzielnie o dwie liczby calkowite
# Podziel te liczby przez siebie
# wyswietl wynik
# sprawdz czy nie zachodzi dzielenie przez zero jezeli tak popros o inna wartosc
# wyswietl komunikt i wynik dzialania

con1 = True
while con1:
    try:
        a = float(input('Podaj pierwszą liczbę: '))
        con1 = False
    except:
        print('Proszę podać liczbę, w której separatorem dzisiętnym jest kropka.')
con2 = True
while con2:
    try:
        b = float(input('Podaj drugą liczbę: '))
        if b == 0:
            print('Dzielnik nie może być zerem.')
        else:
            con2 = False
    except:
        print('Proszę podać liczbę, w której separatorem dzisiętnym jest kropka.')


print(f'Wynik dzielenia to: {a/b}')
