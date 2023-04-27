from random import randint

list_Ran = []
y = 9

# losowanie z wykluczeniem powtorzen
while y > 0:
    x = randint(-20, 20)
    if x not in list_Ran:
        list_Ran.append(x)
        y -= 1
print(list_Ran)

suma = 0
# sumowanie
for i in list_Ran:
    suma += i

print(suma)
silnia = 1

if suma > 0:
    for i in range(suma):
        silnia *= i + 1
    print(silnia)
