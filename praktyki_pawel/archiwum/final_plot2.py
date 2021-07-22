import pandas as pd
import numpy as np
from natsort import index_natsorted, order_by_index
import json
import scipy.optimize as opt

# Baza danych z 1 folderu
pd.options.mode.chained_assignment = None

# Listy przechowywujace dane
list_of_good_types = []
list_of_non_types = []
dictionary_of_values = {}  # Slownik


# Funkcja liniowa-> zwracajaca Y
def f(aa, x, bb):
    return aa * x + bb


# Pierwsza DataFrame
df = pd.read_pickle('data_2.pickle')
df.reset_index(inplace=True, drop=True)
df.dropna(subset=["Unnamed: 6"], axis=0, how='all', inplace=True)
df = df[df["Unnamed: 4"].str.contains("TOTAL") == 0]
df = df[df['Unnamed: 6'] != 0]
df = df.reindex(index=order_by_index(df.index, index_natsorted(df['Unnamed: 3'], reverse=True)))
df['Unnamed: 3'] = df['Unnamed: 3'].str.replace('-REN', '')
df['Unnamed: 4'] = df['Unnamed: 4'].str.replace('X', '*')
df['Unnamed: 3'] = df['Unnamed: 3'].str.replace('-RE', '')
pd.set_option('display.max_rows', df.shape[0] + 1)
df = df.reindex(index=order_by_index(df.index, index_natsorted(df['Unnamed: 4'], reverse=True)))

df[['Hmin', 'Hmax']] = df['Unnamed: 1'].str.split('--', expand=True)
df.reset_index(inplace=True)
a = df['Unnamed: 1'].str.split('--', expand=True)[0]
# a=a.strip()
b = df['Unnamed: 1'].str.split('--', expand=True)[1]
df = df[df["Hmin"].str.contains("TOTAL") == 0]
df = df.drop(df[df['Hmin'] == ' '].index)
df = df.drop(df[df['Hmax'] == ' '].index)
df = df.drop(columns=['Unnamed: 0', 'Unnamed: 9', 'PF15599', 'Unnamed: 1', 'Unnamed: 8', 'C3_23/19_1', 11, 1097.2, 5486,
                      'Unnamed: 2'])
pd.set_option('display.max_rows', df.shape[0] + 1)
df.insert(7, 'H', '')
for index in df.index:
    try:
        df['Types'] = df['Unnamed: 3'] + ' ' + df['Unnamed: 4']
        p = int(df['Hmax'][index]) - int(df['Hmin'][index])
        df['H'][index] = p
        # ['mass'][index]=df['Unnamed: 5'][index]
    except ValueError:
        print(f'Index zly to {index}')
    except TypeError:
        print(f'zly index to{index}')
df = df.drop(columns=['Unnamed: 3', 'Unnamed: 4', 'Unnamed: 6', 'Unnamed: 7', '0 -- 11', 'PF-RD', 'Hmin', 'Hmax'])
df['mass'] = df['Unnamed: 5']
df = df.drop(columns=['Unnamed: 5'])
pd.set_option('display.max_rows', df.shape[0] + 1)
df = df.reindex(index=order_by_index(df.index, index_natsorted(df['Types'], reverse=True)))
# df['Types']=df['Types'].replace('X','*')
df = df.reset_index(drop=True)
print(df.index)
index1 = df.index[-1]
for p in range(0, index1 + 1):
    if p == index1:
        if df['Types'][p] != df['Types'][p - 1]:
            list_of_non_types.append([df['Types'][p], df['H'][p], df['mass'][p]])
    if p == 0:
        if df['Types'][p] != df['Types'][p + 1]:
            list_of_non_types.append([df['Types'][p], df['H'][p], df['mass'][p]])
    if p != 0 and p != index1:
        if df['Types'][p] != df['Types'][p + 1] and df['Types'][p] != df['Types'][p - 1]:
            list_of_non_types.append([df['Types'][p], df['H'][p], df['mass'][p]])
temp_list = []
for p in range(df.index[0], index1 + 1):
    if p == index1:
        if df['Types'][p] == df['Types'][p - 1]:
            temp_list.append([df['Types'][p], df['H'][p], df['mass'][p]])
            list_of_good_types.append(temp_list)
    else:
        if df['Types'][p] == df['Types'][p + 1]:
            temp_list.append([df['Types'][p], df['H'][p], df['mass'][p]])
        if p != df.index[0] and df['Types'][p] == df['Types'][p - 1] and df['Types'][p] != df['Types'][p + 1]:
            temp_list.append([df['Types'][p], df['H'][p], df['mass'][p]])
        if df['Types'][p] != df['Types'][p + 1]:
            if temp_list.__len__() != 0:
                list_of_good_types.append(temp_list)
                temp_list = []
        if p == 0:
            pass
        else:
            if df['Types'][p] != df['Types'][p + 1] and df['Types'][p] != df['Types'][p - 1] and p != 0:
                temp_list = []
print(df)
# WYKRES
X = []
Y = []
Z = []
u_a = 0
u_b = 0
file2 = open('Wyniki_Ost_2_rury.txt', "a+")
for i in range(0, list_of_good_types.__len__()):
    for j in range(0, list_of_good_types[i].__len__()):
        X.append(list_of_good_types[i][j][2])
        Y.append(list_of_good_types[i][j][1])
    if X.__len__() == 1:
        a = None
        b = None
        u_a = None
        u_b = None
        Ydop = Y
    if X.__len__() == 2:
        y2 = Y[1]
        y1 = Y[0]
        x2 = X[1]
        x1 = X[0]
        if x1 == x2:
            Ydop = Y
            a = None
            b = None
            u_a = None
            u_b = None
        else:
            a = (y2 - y1) / (x2 - x1)
            b = (y1 + y2 - a * (x1 + x2)) / 2
            u_a = 0
            u_b = 0
    else:
        X = list(dict.fromkeys(X))
        Y = Y[0:X.__len__()]
        if X.__len__() == 1:
            a = None
            b = None
            u_a = None
            u_b = None
        if X.__len__() == 2:
            y2 = Y[1]
            y1 = Y[0]
            x2 = X[1]
            x1 = X[0]
            if x1 == x2:
                Ydop = Y
                pass
            else:
                a = (y2 - y1) / (x2 - x1)
                b = (y1 + y2 - a * (x1 + x2)) / 2
                u_a = 0  # W przypadku 2 punktow,zawsze można przeprowadzic prostą
                u_b = 0  # a i b są wyznaczone bez żadnych błędów

        else:
            if len(X) != 1:
                try:
                    # z, cov = np.polyfit(X, Y, 1, cov=True)
                    # p = np.poly1d(z)
                    # yp = p(X)  # predicted y values based on fit
                    # a = z[0]
                    # b = z[1]|
                    a = opt.curve_fit(f, X, Y)[0][0]
                    b = opt.curve_fit(f, X, Y)[0][1]
                except TypeError:
                    print(i)
    if a is None and b is None:
        u_a = None
        u_b = None
    else:
        if a != 0 and len(Y) != 2 and X.__len__() != 1:
            dofreedom = len(Y) - 2
            Ydop = [a * i + b for i in X]
            regression_ss = np.sum((Ydop - np.mean(Y)) ** 2)
            residual_ss = np.sum(np.subtract(Y, Ydop) ** 2)
            if dofreedom * np.sum(np.subtract(X, np.mean(X) ** 2)) == 0:
                u_a = None
                u_b = None
            else:
                u_a = np.sqrt(residual_ss / (dofreedom * np.sum((X - np.mean(X)) ** 2)))
                u_b = u_a * np.sqrt(np.sum(np.power(X, 2)) / len(Y))
        else:
            Ydop = Y
    if isinstance(a, float):
        if a == 0:
            file2.write((
                f'{list_of_good_types[i][0][0]}:  a:{a}  b:{b}  u_a:{u_a}  u_b:{u_b}  '
                f'masa:{list_of_good_types[i][0][2]}   '
                f'wysokosc:{f(a, list_of_good_types[i][0][2], b / list_of_good_types.__len__())}  \n'))
        else:
            file2.write((
                f'{list_of_good_types[i][0][0]}:  a:{a}  b:{b}  u_a:{u_a}  u_b:{u_b}  '
                f'masa:{list_of_good_types[i][0][2]}   '
                f'wysokosc:{f(a, list_of_good_types[i][0][2], b)}  \n'))

    else:
        file2.write((
            f'{list_of_good_types[i][0][0]}:  a:{a}  b:{b}  u_a:{u_a}  u_b:{u_b}  '
            f'masa:{list_of_good_types[i][0][2]}   wysokosc:{None}  \n'))
    dictionary_of_values[list_of_good_types[i][0][0]] = [a, b]
    X = []
    Y = []

#print(list_of_good_types)
print(dictionary_of_values)
file2.close()
l_file = json.dumps(dictionary_of_values)
jsonFile = open("dane_drugie.json", "w")
jsonFile.write(l_file)
jsonFile.close()
