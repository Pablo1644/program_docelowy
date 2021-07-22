import pandas as pd

pom=pd.read_excel(r'C:\Users\spektrometr_DAP\Praktyki_Pawel\dane\2003\C1_01_03.xls',skiprows=3)
print(len(pom.columns))