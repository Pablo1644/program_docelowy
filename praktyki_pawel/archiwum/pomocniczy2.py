import math
import os
import pandas
import pandas as pd
import numpy as np
import re


source = r'C:\Users\spektrometr_DAP\Praktyki_Pawel\dane'
list_of_directories = os.listdir(source)
list_of_good_directories=[]  # deklaracja odpowiedniej listy na odpowiednie foldery
list_of_good_files=[]   # deklaracja listy bazujacej na dobrych folderach
for element in list_of_directories:
    prev = os.listdir(source+'\\'+element)
    for j in range(0,prev.__len__()):
        if prev[j].endswith('.doc') or prev[j].endswith('xls') or prev[j].endswith('xlsx'):
            pass
        else:
            list_of_good_directories.append(prev[j])
            temp=os.listdir(source+'\\'+element+'\\'+prev[j])
            for k in range(0, temp.__len__()):
                reg = re.match("^[a-zA-Z][0-9][_][0-9][0-9]", temp[k])  # Dobry regex
                if reg and temp[k].endswith('xls'):
                    list_of_good_files.append(temp[k])

print(list_of_good_files)
# print(list_of_good_files)