import pandas as pd
import math
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import pickle
import os




# Listy przechowywujace dane
list_of_height = []
list_of_mass = []
list_of_types = []
# list_of_data = []

# Funkcje
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


def check_if_number_in_string(word):
    temp = True
    for element in word:
        if element.isspace():
            temp = False
            return temp
        else:
            temp = True
    return temp
# Otworzenie pliku od 6 linii
src = r'C:\Users\spektrometr_DAP\Praktyki_Pawel\dane\LOAD 2020\LOAD 01_20'
filelist = os.listdir(src)
for element in filelist:
    if element.__contains__('CAŁY') or element.endswith('.xlsx'):
        filelist.remove(element)
print(filelist)
df = pd.DataFrame()
for file in filelist:
    #df = df.append(pd.read_excel(file))
    df = df.append(pd.read_excel(src+'\\'+file,skiprows=6))
df = df.replace(0, np.nan)
df.dropna(subset=["Unnamed: 6"],axis=0,how='all',inplace=True)
#df.loc[:, 'C':'E']
list_of_data = df.values.tolist()




df.to_pickle('df.pickle')

dl = list_of_data.__len__()


def data_for_work():
    for j in range(0, dl):
        if isinstance(list_of_data[j][1], float):
            if math.isnan(list_of_data[j][1]) is True:
                pass
        elif isinstance(list_of_data[j][1], str):
            if list_of_data[j][6] ==0:  # puste dane
                pass
            elif get_height(list_of_data[j][1]) is not None:
                list_of_height.append(get_height(list_of_data[j][1]))
        if isinstance(list_of_data[j][6], float) or isinstance(list_of_data[j][6], int):
            if math.isnan(list_of_data[j][6]) is True:
                # list_of_data.pop(j)
                pass
            else:
                if list_of_data[j][6] == 0:  # puste dane
                    pass
                elif list_of_data[j][6]/5 <3000:
                    list_of_mass.append((list_of_data[j][6])/5)  # masa w gramach

        if isinstance(list_of_data[j][3], float):
            if math.isnan(list_of_data[j][3]) is True:
                pass
        else:
                if check_if_number_in_string(list_of_data[j][3]) is True:
                    if list_of_data[j][3] =='SHAPE' or  list_of_data[j][3]== 'HOURS':
                        pass
                    else:
                        list_of_types.append([list_of_data[j][3],list_of_data[j][4]])
                else:
                    pass

#pd.set_option("display.max_rows", None, "display.max_columns", None)
#print(df)
#data_for_work()
#print(list_of_height)
#print(get_height('10'))

#print(list_of_height.__len__())
#print(list_of_types.__len__())
#print(list_of_mass.__len__())


#print(list_of_types)
'''

'''
