import pandas as pd
import matplotlib.pyplot as plt
import math


def isNaN(num):
    return num != num
#print(isNaN('0'))


# Funkcja modyfikujaca wysokosc (typu string) na liczbe
# argumenty string (liczba--liczba)
# Funkcja wyluskuje dana wysokosc z tekstu (ewentualnie do poprawki, w zaleznosci od danych)


def get_height(needed_height):
    wanted_height = ''
    for ch in needed_height:
        if ch.isdigit():
            wanted_height += ch
    b = int(wanted_height[2:])
    a = int(wanted_height[0:2])
    return b - a


# Funkcja pokazujaca pomocniczy wykres
def show_graph():
    plt.title('Wykres dla naszych danych')
    plt.ylabel('Wysokosc')
    plt.xlabel('Waga kamienii')
    plt.plot(list_of_height, list_of_mass)
    plt.scatter(list_of_height, list_of_mass, marker='o')
    for m in range(list_of_height.__len__()):
        plt.annotate(list_of_types[m],
                     xy=(list_of_height[m]+400,list_of_mass[m]),
                     xytext=(list_of_height[m]+400, list_of_mass[m]))

    #plt.legend()
    plt.show()

# pierwsza czesc programu polegajaca na tym,ze otwieramy dany plik i odpowiadajace sobie wartosci
# uporządkowywujemy przy pomocy list
data = pd.read_excel(r"C:\Users\pawel\OneDrive\Dokumenty\praktyki_pawel\Zeszyt1.xls", skipfooter=4)
list_of_data = data.values.tolist()

# Tworzymy miejsce na liste wysokosci oraz liste mas (pusta lista)
list_of_height = []
list_of_mass = []
list_of_types = []
# Petla uporzadkowywujaca odpowiednie elementy w listy,po przejsciu mamy liste mas i liste wag
for element in list_of_data:
    if element[0]:
        list_of_mass.append(element[0])
    if element[1]:
        list_of_height.append(element[1])
    if element[2]:
        list_of_types.append(element[2])

#show_graph()
#int('25.6')
#'56'.isnumeric()
#print(math.isnan(float('nan')))
#print(math.isnan(float(get_height('10--9392'))))

# print(math.isnan(float('kok')))
# test = isinstance('Kon',str)
# print(test)
print(list_of_height[0])
print(isinstance('', float))