import pandas as pd
from scipy import optimize
from natsort import index_natsorted, order_by_index

# Baza danych z 1 folderu
pd.options.mode.chained_assignment = None

# Listy przechowywujace dane
list_of_height = []
list_of_mass = []
list_of_good_types = []

list_of_height2 = []
list_of_mass2 = []
list_of_good_types2 = []

list_of_non_types = []

# Funkcja odczytujaca wysokosc ze stringa,
# gdzie argumentem jest szukana wysokosc,zwracajaca wysokosc jako int (int
# minus int)


def get_height(needed_height):
    wanted_height = ''
    for ch in needed_height:
        if ch.isdigit():
            wanted_height += ch
    if wanted_height == '':
        return None
    if wanted_height.__len__() == 2:
        a = int(wanted_height)
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
    if isinstance(needed_height, int):
        return None
    else:
        wanted_height = needed_height.split(' -- ')
        return wanted_height


def check_if_number_in_string(word):
    temp = True
    if isinstance(word, int):
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


# Pierwsza DataFrame
# df = pd.DataFrame()
# df2 = pd.DataFrame()
df = pd.read_pickle('data_1.pickle')
df.reset_index(inplace=True, drop=True)
df.dropna(subset=["Unnamed: 6"], axis=0, how='all', inplace=True)
df = df[df["Unnamed: 4"].str.contains("TOTAL") == False]
df = df[df['Unnamed: 6'] != 0]
df = df.reindex(index=order_by_index(df.index, index_natsorted(df['Unnamed: 3'], reverse=True)))
df['Unnamed: 3'] = df['Unnamed: 3'].str.replace('-REN', '')
df['Unnamed: 3'] = df['Unnamed: 3'].str.replace('-RE', '')
pd.set_option('display.max_rows', df.shape[0] + 1)
df = df.reindex(index=order_by_index(df.index, index_natsorted(df['Unnamed: 4'], reverse=True)))

# print(df.columns)



df[['Hmin', 'Hmax']] = df['Unnamed: 1'].str.split('--', expand=True)
df.reset_index(inplace=True)
a = df['Unnamed: 1'].str.split('--', expand=True)[0]
# a=a.strip()
b = df['Unnamed: 1'].str.split('--', expand=True)[1]
df = df[df["Hmin"].str.contains("TOTAL") == False]
df = df.drop(df[df['Hmin'] == ' '].index)
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
# df['Types'] = df['Types'].str.replace('-REN', '')
# df['Types'] = df['Types'].str.replace('-RE', '')
#



#df = df.rename(columns={'Unnamed 1': 'Col_1'},inplace=True)

df = df.reset_index(drop=True)
index1 = df.index[-1]
df = df.drop(columns=['Unnamed: 0','Unnamed: 1','Unnamed: 7','Unnamed: 8','Unnamed: 2' ,'Unnamed: 3','Unnamed: 4',
                      'Unnamed: 6','index','Hmin','Hmax'])
df['mass']=df['Unnamed: 5']
df = df.drop(columns=['Unnamed: 5'])
df = df.drop(columns=['Unnamed: 9'])

index1 = df.index[-1]
for p in range(0, index1+1):
    if p == index1:
        if df['Types'][p] != df['Types'][p - 1]:
            list_of_non_types.append([df['Types'][p], df['H'][p], df['mass'][p]])
    if p == 0:
        if df['Types'][p] != df['Types'][p+1]:
            list_of_non_types.append([df['Types'][p], df['H'][p], df['mass'][p]])
    if p != 0 and p != index1:
        if df['Types'][p] != df['Types'][p + 1] and df['Types'][p] != df['Types'][p - 1]:
            list_of_non_types.append([df['Types'][p], df['H'][p], df['mass'][p]])
temp_list = []
for p in range(df.index[0], index1+1):
    if p == index1:
        if df['Types'][p] == df['Types'][p-1]:
            temp_list.append([df['Types'][p], df['H'][p], df['mass'][p]])
            list_of_good_types.append(temp_list)
    else:
        if df['Types'][p] == df['Types'][p + 1]:
            temp_list.append([df['Types'][p], df['H'][p], df['mass'][p]])
        if p != df.index[0] and df['Types'][p] == df['Types'][p-1] and df['Types'][p] != df['Types'][p+1]:
            temp_list.append([df['Types'][p], df['H'][p], df['mass'][p]])
        if df['Types'][p] != df['Types'][p+1]:
            if temp_list.__len__()!=0:
                list_of_good_types.append(temp_list)
                temp_list = []
        if df['Types'][p] != df['Types'][p + 1] and df['Types'][p] != df['Types'][p - 1] and p != df.index[0]:
            temp_list = []



# [['RG MX', 11, 665.4], ['RG MX', 15, 1191.1], ['RG MX', 16, 1347.5], ['RG MX', 18, 1465.3], ['RG MX', 10, 700.1]]
# Dlatego pierwszy parametr to bedzie i -> iterator

# 0-> typ 1->wysokosc 2->masa
for i in range(0,list_of_good_types.__len__()):
    print(list_of_good_types[i])
    for j in range(0,list_of_good_types[i].__len__()):
        print(list_of_good_types[i][j][0])

