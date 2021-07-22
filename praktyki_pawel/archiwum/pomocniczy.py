import math
import os
import pandas
import pandas as pd
import numpy as np
import re



source = r'C:\Users\spektrometr_DAP\Praktyki_Pawel\dane\LOAD 2020'
list_of_directories = os.listdir(source)
list_of_good_files=[]
for element in list_of_directories:
     temp=os.listdir(source+'\\'+element)
     for k in range(0,temp.__len__()):
         reg = re.match("^[a-zA-Z][0-9]", temp[k])  # Dobry regex
         if reg and temp[k].endswith('xls'):
             list_of_good_files.append(temp[k])
print(list_of_directories)
print(list_of_good_files)
#lista=['a','b','c','d']
#for k,l in enumerate(lista):
#    print(k,l)

#checking_list=["D2_5","A3_8","LOAD20","CALY LOAD 2020"]
#print(isinstance(checking_list[0],str))
#for elem in range(checking_list.__len__()):
#    reg = re.match("^[a-zA-Z][0-9]", checking_list[elem])   # Dobry regex
#    if reg:
#        print(checking_list[elem])

#print(reg)