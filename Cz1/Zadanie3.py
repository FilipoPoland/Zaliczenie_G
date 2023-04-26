# za pomoca jednego input
# popros jednym pytaniem o liczby odzielone przecinkami
# podnies liczby nieparzyste do potegi 3 a parzyste 2
# zsumuj podniesione do potegi liczby
# wynik wyswietl z komunikatem

u_input = input('Podaj liczby oddzielone przecinkami, separator dziesiętny to kropka: ')

# w razie gdyby użytkownik podał spacje
u_input = u_input.replace(' ', '')
# stworzenie listy
u_list = u_input.split(',')

# listy parzystych i nie parzystych
p_list = []
np_list = []
s_list = []

for i in range(len(u_list)):
    try:
        if float(u_list[i]) % 2 == 0:
            p_list.append(u_list[i])
        else:
            u_list[i] = float(u_list[i])
            np_list.append(u_list[i])
    except:
        print('Została podana nie poprawna wartość.')

for i in range(len(p_list)):
    c = float(p_list[i]) ** 2
    s_list.append(c)

for i in range(len(np_list)):
    c = float(np_list[i]) ** 3
    s_list.append(c)

suma = 0

for i in range(len(s_list)):
    suma += s_list[i]

print(suma)