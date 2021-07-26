import json

file = open("dane_koncowe_2.json")
wspolczynniki = json.load(file)


def fun(type_of_stone):
    while True:
        try:
            mass = float(input('Podaj mase:'))
            break
        except ValueError:
            print('ERROR: podaj inna mase')
    a, b = wspolczynniki[type_of_stone]
    print(f'Dla {type_of_stone}, wysokość wynosi: {a * mass + b}')
    return a * mass + b


try:
    fun("RG-FAR 9~12")
except ValueError:
    print('Podaj inna mase')
