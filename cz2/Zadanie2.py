u_input = input('Podaj jedną literę: ')
list_name = ['Ala', 'Marek', 'Ola', 'Mariusz', 'Paweł', 'Anna', 'Iwo']
list_name1 =[]

for i in list_name:
    if len(i) < 5:
        if i[-1] == u_input:
            list_name1.append(i)

print(list_name1)
