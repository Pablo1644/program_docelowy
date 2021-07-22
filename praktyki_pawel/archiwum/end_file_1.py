import json

file = open("dane_pierwsze.json")
wspolczynniki = json.load(file)
file_for_results = open('koncowe_wyniki1_Pawel.txt', 'w+')


def fun(type_of_stone, mass=float(input('Podaj mase'))):
    a, b = wspolczynniki[type_of_stone]
    print(b)
    return a * mass + b


print(fun('RD'))
