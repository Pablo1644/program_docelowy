import pandas as pd
from scipy import optimize as opt
import numpy as np
import matplotlib.pyplot as plt
from natsort import index_natsorted, order_by_index


# Baza danych z 1 folderu
pd.options.mode.chained_assignment = None

# Listy przechowywujace dane
list_of_good_types = []
list_of_non_types = []


# Funkcja liniowa-> zwracajaca Y
def f(a,x,b):
    return a*x+b


# Pierwsza DataFrame
df = pd.read_pickle('data_2.pickle')
df.reset_index(inplace=True, drop=True)
df.dropna(subset=["Unnamed: 6"], axis=0, how='all', inplace=True)
df = df[df["Unnamed: 4"].str.contains("TOTAL") == False]
df = df[df['Unnamed: 6'] != 0]
df = df.reindex(index=order_by_index(df.index, index_natsorted(df['Unnamed: 3'], reverse=True)))
df['Unnamed: 3'] = df['Unnamed: 3'].str.replace('-REN', '')
df['Unnamed: 3'] = df['Unnamed: 3'].str.replace('-RE', '')
pd.set_option('display.max_rows', df.shape[0] + 1)
df = df.reindex(index=order_by_index(df.index, index_natsorted(df['Unnamed: 4'], reverse=True)))


df[['Hmin', 'Hmax']] = df['Unnamed: 1'].str.split('--', expand=True)
df.reset_index(inplace=True)
a = df['Unnamed: 1'].str.split('--', expand=True)[0]
# a=a.strip()
b = df['Unnamed: 1'].str.split('--', expand=True)[1]
df = df[df["Hmin"].str.contains("TOTAL") == False]
df = df.drop(df[df['Hmin'] == ' '].index)
df = df.drop(df[df['Hmax'] == ' '].index)
df = df.drop(df[df['Hmin'] == '32- - 46'].index)
df.insert(7, 'H', '')

for index in df.index:
    try:
        df['Types'] = df['Unnamed: 3'] + ' ' + df['Unnamed: 4']
        p = int(df['Hmax'][index]) - int(df['Hmin'][index])
        df['H'][index] = p
    except ValueError:
        print(f'Index zly to {index}')
    except TypeError:
        print(f'zly index to{index}')


pd.set_option('display.max_rows', df.shape[0] + 1)
df = df.reindex(index=order_by_index(df.index, index_natsorted(df['Types'], reverse=True)))


df = df.reset_index(drop=True)
index1 = df.index[-1]
df = df.drop(columns=['Unnamed: 0','Unnamed: 1','Unnamed: 7','Unnamed: 8','Unnamed: 2' ,'Unnamed: 3','Unnamed: 4',
                      'Unnamed: 6','index','Hmin','Hmax'])
df['mass']=df['Unnamed: 5']
df = df.drop(columns=['Unnamed: 5'])
df = df.drop(columns=['Unnamed: 9'])


index1 = df.index[-1]
print(index1)