while True:
    try:
        liczba=int(input('Podaj liczbe parzystą większą od 20'))
    except:
        print('Podaj inną wartość')
    if liczba %2==0:
        if liczba>20:
            break
wyniki=[]
print(f'Liczby pierwsze do liczba podana to {liczba}')
for i in range(2,liczba+1):
    for j in wyniki:
        if i % j == 0:
            break
    else:
        wyniki.append(i)
        print(i)

