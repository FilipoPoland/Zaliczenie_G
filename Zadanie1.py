# za pomoca jednego input pobierz wartosci a b i c do funkcji kwadratowej
# oblicz miejsca zerowe
# wyswietl wyniki do dwoch miejsc po przecinku
# podaj ile jest miejsc zerowych w komunikacie

from math import sqrt
c = True
while c:
    u_input = input('Podaj współczynniki funkcji kwadratowej odzielone przecinkami w klejności a, b, c (separator '
                    'dziesiętny to kropka): ')
    # w razie gdyby użytkownik podał spacje
    u_input = u_input.replace(' ', '')
    # stworzenie listy
    u_list = u_input.split(',')

    try:
        delta = (float(u_list[1]) ** 2) - (4 * float(u_list[0]) * float(u_list[2]))
        if delta < 0:
            print('Brak miejsc zerowych.')

        elif delta == 0:

            print('Jedno miejsce zerowe')
        elif delta > 0:
            x1 = (-(float(u_list[1])) + sqrt(delta)) / (2 * float(u_list[0]))
            x2 = (-(float(u_list[1])) - sqrt(delta)) / (2 * float(u_list[0]))
            # zaokraglenie
            x1 = round(x1, 2)
            x2 = round(x2, 2)
            print(f'Dwa miejscza zerowe: {x1} oraz {x2}')
            c = False
    except:
        print('Zostały podane błędne wartości.')


