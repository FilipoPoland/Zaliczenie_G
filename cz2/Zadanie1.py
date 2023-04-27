while True:
    while True:
        try:
            dol = int(input('Podaj dolna wartosc zakresu: '))
            break
        except:
            continue
    while True:
        try:
            gora = int(input('Podaj gorna wartosc zakresu: '))
            break
        except:
            continue
    if dol < gora:
        break


