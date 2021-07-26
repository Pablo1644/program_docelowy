import json
import pandas as pd
from scipy import optimize as opt
import numpy as np
from natsort import index_natsorted, order_by_index


# Funkcja liniowa-> zwracajaca Y
def f(aa, x, bb):
    if x is None:
        return None
    return aa * x + bb


# Baza danych z 1 folderu
pd.options.mode.chained_assignment = None

# Listy przechowywujace dane
list_of_good_types = []
list_of_non_types = []
list_for_dict = []
dictionary_of_values = {}  # Slownik
df = pd.read_pickle('data_n_2.pickle')
pd.set_option('display.max_rows', df.shape[0] + 1)
df['Shape'] = df['Shape'].str.replace('-REN', '')
df['Shape'] = df['Shape'].str.replace('-RE', '')
df['Height'] = df['Height'].str.replace('--', '-')
df['Size'] = df['Size'].str.replace('X', '*')
df['Height'] = df['Height'].str.replace(' -', ' - ')
df['Height'] = df['Height'].str.replace('  - ', ' - ')
df['Height'] = df['Height'].str.replace(' -  ', ' - ')
df['Height'] = df['Height'].str.replace(' _ ', ' - ')
# df['Height'] = df['Height'].str.replace('_','')
# df['Height'] = df['Height'].str.replace(' _ ',' - ')
# df['Height'] = df['Height'].str.replace(' -10',' - 10')
# df['Height'] = df['Height'].str.replace('  ',' - ')


df = df.reindex(index=order_by_index(df.index, index_natsorted(df['Size'], reverse=True)))
pd.set_option('display.max_rows', df.shape[0] + 1)
df.dropna(subset=["Mass"], axis=0, how='any', inplace=True)
pd.set_option('display.max_rows', df.shape[0] + 1)
df[['Hmin', 'Hmax']] = df['Height'].str.split(' - ', expand=True)
df.insert(6, 'H', '')
df = df.reset_index(drop=True)
for index in df.index:
    try:
        df['Types'] = df['Shape'] + ' ' + df['Size']
        p = float(df['Hmax'][index]) - float(df['Hmin'][index])
        df['H'][index] = p
    except ValueError:
        print(f'Index zly to {index}')
        print(df['Hmax'][index])
    except TypeError:
        print(f'Zly index:{index}')  # Najwyzej dmy split [0] i split[1]
        # df[['Hmin', 'Hmax']][index] = df['Height'][index].str.split('  ', expand=True)
        print(df['Height'][index])

df = df.drop(columns=['Size', 'Shape', 'Height'])
df = df.reset_index(drop=True)
df = df.reindex(index=order_by_index(df.index, index_natsorted(df['Types'], reverse=True)))
temp_list = []
df = df.reset_index(drop=True)
index1 = df.index[-1]
for p in range(df.index[0], index1):
    if p == index1:
        if df['Types'][p] == df['Types'][p - 1]:
            temp_list.append([df['Types'][p], df['H'][p], df['Mass'][p]])
            list_of_good_types.append(temp_list)
    if p == 0:
        if df['Types'][p] == df['Types'][p + 1]:
            temp_list.append([df['Types'][p], df['H'][p], df['Mass'][p]])
    else:
        if df['Types'][p] == df['Types'][p + 1]:
            temp_list.append([df['Types'][p], df['H'][p], df['Mass'][p]])

        if p != df.index[0] and df['Types'][p] == df['Types'][p - 1] and df['Types'][p] != df['Types'][p + 1]:
            temp_list.append([df['Types'][p], df['H'][p], df['Mass'][p]])
        if df['Types'][p] != df['Types'][p + 1]:
            if temp_list.__len__() != 0:
                list_of_good_types.append(temp_list)
                temp_list = []
        if df['Types'][p] != df['Types'][p + 1] and df['Types'][p] != df['Types'][p - 1] and p != 0:
            temp_list = []

# print(list_of_good_types)
# # # WYKRES
X = []
Y = []
Z = []
u_a, u_b = 0, 0
j, a, b = 0, 0, 0
file2 = open('Wyniki_Ostateczne_2_rury.txt', "a+")
for i in range(0, list_of_good_types.__len__()):
    for j in range(0, list_of_good_types[i].__len__()):
        X.append(float(list_of_good_types[i][j][2]))
        Y.append(float(list_of_good_types[i][j][1]))
    X = list(dict.fromkeys(X))
    Y = Y[0:X.__len__()]
    if X.__len__() == 2:
        y2 = Y[1]
        y1 = Y[0]
        x2 = X[1]
        x1 = X[0]
        if x1 == x2:
            Ydop = Y
        else:
            a = (y2 - y1) / (x2 - x1)
            b = (y1 + y2 - a * (x1 + x2)) / 2
            u_a = 0  # W przypadku 2 punktow,zawsze można przeprowadzic prostą
            u_b = 0  # a i b są wyznaczone bez żadnych błędów
            file2.write(
                f'{list_of_good_types[i][0][0]}:  a:{a}  b:{b}  u_a:{u_a}  u_b:{u_b}  \n')
    if X.__len__() == 1 or Y.__len__() == 1:
        a, b, u_a, u_b = None, None, None, None
    if Y.__len__() > 2:
        a = opt.curve_fit(f, X, Y)[0][0]
        b = opt.curve_fit(f, X, Y)[0][1]
        dofreedom = len(Y) - 2
        Ydop = [a * i + b for i in X]
        regression_ss = np.sum((Ydop - np.mean(Y)) ** 2)
        residual_ss = np.sum(np.subtract(Y, Ydop) ** 2)
        u_a = np.sqrt(residual_ss / (dofreedom * np.sum((X - np.mean(X)) ** 2)))
        u_b = u_a * np.sqrt(np.sum(np.power(X, 2)) / len(Y))
        file2.write(
            f'{list_of_good_types[i][j][0]}:  a:{a}  b:{b}  u_a:{u_a}  u_b:{u_b}  \n')

    dictionary_of_values[list_of_good_types[i][0][0]] = [a, b]
    X = []
    Y = []

file2.close()

l_file = json.dumps(dictionary_of_values)
jsonFile = open("dane_koncowe_2.json", "w")
jsonFile.write(l_file)
jsonFile.close()
