import json

file = open("dane_drugie.json")
wspolczynniki = json.load(file)
file_for_results = open('koncowe_wyniki1_Pawel.txt', 'w+')
for k in wspolczynniki.keys():
    a = wspolczynniki[k][0]
    b = wspolczynniki[k][1]
    while True:
        try:
            mass = float(input(f'Podaj mase dla {k} :'))
            break
        except ValueError:
            print('Podales zla wartosc')
    if a is not None:
        height = a * mass + b
        print(f'{k} dla a={a}, b={b}, masy:{mass}    wysokosc:{height}')
        file_for_results.write(f'{k} dla a={a},b={b},masy={mass}   wysokosc:{height}')
    else:
        file_for_results.write(f'{k} dla a={a},b={b},masy={mass}   wysokosc:{None}')
        print(f'{k} dla a={a}, b={b}, masy:{mass}    wysokosc:{None}')
