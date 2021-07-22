import pandas
import pandas as pd
import math
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import pickle
import os
import re
from natsort import index_natsorted, order_by_index
# Baza danych z 1 folderu
pd.options.mode.chained_assignment = None

# Listy przechowywujace dane
list_of_height = []
list_of_mass = []
list_of_types = []
list_of_data = []
list_of_bugs=[]
# Funkcja odczytujaca wysokosc ze stringa,gdzie argumentem jest szukana wysokosc,zwracajaca wysokosc jako int (int minus int)

def get_height(needed_height):
    wanted_height = ''
    for ch in needed_height:
        if ch.isdigit():
            wanted_height += ch
    if wanted_height == '':
        return None
    if wanted_height.__len__()==2:
        a =int(wanted_height)
        return a
    if wanted_height[0] == '0':
        a = int(wanted_height[0])
        b = int(wanted_height[1:])
    else:
        b = int(wanted_height[2:])
        a = int(wanted_height[0:2])
    return b - a
# Funkcja zwracająca liste stringow z wysokosci
def get_height2(needed_height):
    if isinstance(needed_height,int):
        return None
    else:
        wanted_height=needed_height.split(' -- ')
        return wanted_height

def check_if_number_in_string(word):
    temp = True
    if isinstance(word,int):
        return False
    for element in word:
        if element.isspace():
            temp = False
            return temp
        else:
            temp = True
    return temp

def return_string(word):
    return int(word)

df = pd.DataFrame()
source = r'C:\Users\spektrometr_DAP\Praktyki_Pawel\dane'



df=pd.read_pickle('df2.pickle')
list_of_data2 = df.values.tolist()
#print(list_of_data2[10])
#a=list_of_data2.__len__
#print(a)
df.reset_index(inplace=True,drop=True)
df.dropna(subset=["Unnamed: 6"],axis=0,how='all',inplace=True)
# print(df.columns)

df=df[df["Unnamed: 4"].str.contains("TOTAL")==False]
df= df[df['Unnamed: 6'] != 0]
pd.set_option("display.max_rows", 12, "display.max_columns", None)
#df.insert(4,'Height','')


list_of_data = df.values.tolist()
#print(list_of_data)
dl = list_of_data.__len__()
def data_for_work():
    list_of_height.append(21)
    for j in range(0, dl):

        if isinstance(list_of_data[j][1], str):
            #list_of_height.append(5)
            list_of_height.append(get_height(list_of_data[j][0]))
        if isinstance(list_of_data[j][0], str):
            if isinstance(list_of_data[j][3], float) or isinstance(list_of_data[j][3], int) :
                list_of_mass.append((list_of_data[j][3])/5)  # masa w gramach

        if isinstance(list_of_data[j][1], float):
            if math.isnan(list_of_data[j][1]) is True:
                pass
        else:
                if check_if_number_in_string(list_of_data[j][1]) is True:
                    if list_of_data[j][1] =='SHAPE' or  list_of_data[j][1]== 'HOURS':
                        pass
                    else:
                        if isinstance(list_of_data[j][0], str):
                            if isinstance(list_of_data[j][2], str):
                                list_of_data[j][2]=list_of_data[j][2].replace('X','*')
                            print('DODAJE TYPA')
                            list_of_types.append([list_of_data[j][1],list_of_data[j][2]])
                else:
                    pass


data_for_work()
#print(list_of_height)
p =list_of_data.__len__()
k = 0

df[['Hmin','Hmax']] = df['Unnamed: 1'].str.split('--',expand=True)
df.reset_index(inplace=True)
a=df['Unnamed: 1'].str.split('--',expand=True)[0]
#a=a.strip()
b=df['Unnamed: 1'].str.split('--',expand=True)[1]
df=df[df["Hmin"].str.contains("TOTAL")==False]
df = df.drop(df[df['Hmin']==' '].index)
df = df.drop(df[df['Hmin']=='32- - 46'].index)
df = df.drop(df[df['Hmax']==' '].index)
frames=[df['Unnamed: 3'],df['Unnamed: 4']]
result=pd.concat(frames)
df=df.drop(columns=['Unnamed: 8','Unnamed: 0','Unnamed: 6','Unnamed: 7','Unnamed: 9','Unnamed: 2'])
df.insert(7,'H','')


for index in df.index:
    try:
        df['Types']=df['Unnamed: 3']+' '+df['Unnamed: 4']
        p=int(df['Hmax'][index]) - int(df['Hmin'][index])

        df['H'][index]=p
    except ValueError :
        print(f'Index zly to {index}')
    except TypeError:
        print(f'zly index to{index}')
df=df.drop(columns=['Unnamed: 3','Unnamed: 4'])
#print(df)

pd.set_option('display.max_rows', df.shape[0]+1)
#print(df['Types'])
# if df['Types'][0]==df['Types'][1]:
#     print('YES')
# else:
#     print('NO')
pd.set_option('display.max_rows', df.shape[0]+1)
df = df.reindex(index=order_by_index(df.index, index_natsorted(df['Types'], reverse=True)))
print(df)
#print(df2)
#df=df.drop(columns=['Unnamed: 8','Unnamed: 0','Unnamed: 6','Unnamed: 7','Unnamed: 9','Unnamed: 2'])
#print(df)


#print(df)

#print(result[1])
#print(df)
# try:
#     #df['H']='P'
#
# except ValueError:
#     pass
#df.dropna(subset=["Hmin"],axis=0,how='any',inplace=True)
#df['H']=df['Unnamed: 1'].str.split('--',expand=True)[0].astype(int)


#df.to_csv('df2.csv')