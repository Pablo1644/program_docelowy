import pandas as pd
import math
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import pickle
import os
import re
# Baza danych z 1 folderu


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



df = pd.DataFrame()
source = r'C:\Users\spektrometr_DAP\Praktyki_Pawel\dane'
list_of_directories = os.listdir(source)
list_of_good_directories=[]  # deklaracja odpowiedniej listy na odpowiednie foldery
list_of_good_files=[]   # deklaracja listy bazujacej na dobrych folderach

for element in list_of_directories:
    prev = os.listdir(source+'\\'+element)
    #print(element,prev)
    #print(prev)
    for j in range(0,prev.__len__()):
        if prev[j].endswith('xls'):
            print(prev[j])
            list_of_good_directories.append(prev[j])
            temp = (source + '\\' + element + '\\' + prev[j])
            #print(temp)
            for k in range(0, temp.__len__()):
                #print(prev[j])
                #print(temp)
                reg = re.match("^[a-zA-Z][1][_][0-9][0-9][_][0-9][0-9]", temp)  # Dobry regex
                if reg:
                    list_of_good_files.append(temp)
                    print(temp)
                    size=list_of_good_files.__len__()
                    df = (pd.read_excel(source+'\\'+element+'\\'+prev[j]+'\\'+list_of_good_files[size-1],skiprows=6))

pd.set_option('display.max_rows',None)
#print(list_of_good_directories)
#print(df)
list_of_data = df.values.tolist()
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
                        if isinstance(list_of_data[j][4], str):
                            list_of_data[j][4]=list_of_data[j][4].replace('X','*')
                        list_of_types.append([list_of_data[j][3],list_of_data[j][4]])
                else:
                    pass



#data_for_work()
# print(list_of_mass.__len__())
# print(list_of_height.__len__())
# print(list_of_types.__len__())
# # print(df.columns)
# cols_to_drop=['Unnamed: 0','Unnamed: 2','Unnamed: 5','Unnamed: 7','Unnamed: 8','Unnamed: 9','C3_23/19_1',
#           '0 -- 11',      'PF-RD',           11,       1097.2,         5486,
#           'PF15599']
# df=df.drop(cols_to_drop,axis=1)
print(df)
print(df.index)

df.to_pickle('data_1.pickle')
df.to_csv('data_1.csv')

# print(pd.read_pickle('df2.pickle'))