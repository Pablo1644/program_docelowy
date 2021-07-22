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
list_temp = []
list_of_good_files=[]
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


#wersja z 1 plikiem
#df = pd.read_excel(src)
#src = r'C:\Users\spektrometr_DAP\Praktyki_Pawel\dane\LOAD 2020\LOAD 01_20\CAŁY LOAD 01_20.xls'
#df = df.replace(0, np.nan)
#df.dropna(subset=["Unnamed: 6"],axis=0,how='all',inplace=True)
#pd.set_option("display.max_rows", None, "display.max_columns", None)
#print(df)
#list_of_data = df.values.tolist()


src = r'C:\Users\spektrometr_DAP\Praktyki_Pawel\dane\LOAD 2020'
prev_list=os.listdir(src)
#print(prev_list)
for el in range(0,prev_list.__len__()):
        list_temp.append(os.listdir(src + '\\' + prev_list[el]))
#print(list_temp)
print(list_temp[0][0])
#for elem in list_temp:
    #print(isinstance(list_temp[elem],str))
    #reg = re.match("^[a-zA-Z][0-9][_]", list_temp[elem])
    #if reg:
        #list_of_good_files.append(list_temp[elem])
        #reg = re.match("^[a-zA-Z][0-9][_][0-9][0-9]", list_temp[el])
#print(list_temp[3])
    # for element in filelist:
    #     reg = re.match("^[a-zA-Z][0-9][_][0-9][0-9]",element)
    #     if reg and element.endswith('xls') and element.__contains__('CAŁY') is not True:
    #         list_of_good_files.append(element)
    #     else:
    #         pass
    # print(list_of_good_files)
    # df = pd.DataFrame()
    # for file in filelist:
    #     df = df.append(pd.read_excel(src+'\\'+filelist[el]+'\\'+file,skiprows=6))

    #list_of_data = df.values.tolist()

#df.to_pickle('df.pickle')

# dl = list_of_data.__len__()


# def data_for_work():
#
#     for j in range(0, dl):
#         if isinstance(list_of_data[j][1], float):
#             if math.isnan(list_of_data[j][1]) is True:
#                 pass
#         elif isinstance(list_of_data[j][1], str):
#             if list_of_data[j][6] ==0:  # puste dane
#                 pass
#             elif get_height(list_of_data[j][1]) is not None:
#                 list_of_height.append(get_height(list_of_data[j][1]))
#         if isinstance(list_of_data[j][6], float) or isinstance(list_of_data[j][6], int):
#             if math.isnan(list_of_data[j][6]) is True:
#                 # list_of_data.pop(j)
#                 pass
#             else:
#                 if list_of_data[j][6] == 0:  # puste dane
#                     pass
#                 elif list_of_data[j][6]/5 <3000:
#                     list_of_mass.append((list_of_data[j][6])/5)  # masa w gramach
#
#         if isinstance(list_of_data[j][3], float):
#             if math.isnan(list_of_data[j][3]) is True:
#                 pass
#         else:
#                 if check_if_number_in_string(list_of_data[j][3]) is True:
#                     if list_of_data[j][3] =='SHAPE' or  list_of_data[j][3]== 'HOURS':
#                         pass
#                     else:
#                         if isinstance(list_of_data[j][4], str):
#                             list_of_data[j][4]=list_of_data[j][4].replace('X','*')
#                         list_of_types.append([list_of_data[j][3],list_of_data[j][4]])
#                 else:
#                     pass
#
#
# data_for_work()
#
#print(list_of_height.__len__())
#print(list_of_types.__len__())
#print(list_of_mass.__len__())

#
# print(list_of_types)
#

