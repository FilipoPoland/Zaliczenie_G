imiona=input('Podaj imiona rozdzielone przecinkiem')
imiona = imiona.lower()

imie =imiona.split(',')
print(imie)

litera=input('Podaj pojedyncza litere')
litera=litera.lower()

print('Wystepuje na poczatku')
for i in imie:
    if litera == i[0]:
        for j in range(1):
            print(i)

print('Wystepuje na początku i koncu')
for i in imie:
    if litera == i[0]:
        x = True
    else:
        x = False

    if litera == i[-1]:
        y = True
    else:
        y = False
    if x and y:
        print(i)

print('Wystepuje na koncu')
for i in imie:
    if litera == i[-1]:
        print(i)
