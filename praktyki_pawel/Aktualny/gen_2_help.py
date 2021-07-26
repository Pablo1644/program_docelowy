import pandas as pd
import math
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import pickle
import os
import re
# Baza danych z 1 folderu
pd.options.mode.chained_assignment = None  # default='warn'

# Listy przechowywujace dane
list_of_height = []
list_of_mass = []
list_of_types = []
appended_data = []

all_data=pd.DataFrame()
df = pd.DataFrame()
source = r'C:\Users\spektrometr_DAP\Praktyki_Pawel\dane'
list_of_directories = os.listdir(source)
list_of_good_directories=[]  # deklaracja odpowiedniej listy na odpowiednie foldery
list_of_good_files=[]   # deklaracja listy bazujacej na dobrych folderach

pd.set_option('display.max_columns',8)
for element in list_of_directories:
    prev = os.listdir(source+'\\'+element)
    # print(prev)
    for j in range(0,prev.__len__()):
        reg = re.match("^[a-zA-Z][2,3,4][_][0-9][0-9][_][0-9][0-9]", prev[j])
        if prev[j].endswith('.xls') and reg:
            list_of_good_files.append(prev[j])
            reg = re.match("^[a-zA-Z][1][_][0-9][0-9][_][0-9][0-9]",prev[j])
            df= df.append(pd.read_excel(source+'\\'+element+'\\'+prev[j],skiprows=3),ignore_index=True, sort=False)
pd.set_option('display.max_rows', df.shape[0] + 1)

#print(df.columns)
#print(df)
drop_col = ['Unnamed: 0', 'Unnamed: 2','Unnamed: 6',
          'Unnamed: 7','No.', 'HEIGH, CM', 'ORIGIN',
       'SHAPE', 'SIZE', 'GRAMS', 'NOTES', 'Unnamed: 8']
df=df.drop(columns=drop_col)
df.dropna(subset=["Unnamed: 1"], axis=0, how='all', inplace=True)
df.reset_index(inplace=True)
df = df[df['Unnamed: 5'] != 0]
df = df[df['Unnamed: 5'] != 'GRAMS']
df['Height']=df['Unnamed: 1']
df['Shape']=df['Unnamed: 3']
df['Size']=df['Unnamed: 4']
df['Mass']=df['Unnamed: 5']
df = df.drop(columns=['Unnamed: 1', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5'])
for index in df.index:
    reg = re.match("^[0-9][,][0-9][0-9][0-9]", str(df['Mass'][index]))
    if reg:
        #print(df['Mass'][index])
        p=str(df['Mass'][index])
        p=p.replace(',','')
        try:
            df['Mass'][index]=float(p)
        except ValueError:
            df['Mass'][index]=1180.0
    if isinstance(df['Mass'][index],str) is True:
        df['Mass'][index] = df['Mass'][index].replace('1 ','1')
        df['Mass'][index] = float(df['Mass'][index].replace('2 ', '2'))
df.to_pickle('data_n_2.pickle')
