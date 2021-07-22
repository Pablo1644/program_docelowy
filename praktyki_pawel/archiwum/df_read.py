import pandas as pd

df=pd.read_pickle('df2.pickle')
df.reset_index(inplace=True,drop=True)
df.dropna(subset=["Unnamed: 6"],axis=0,how='all',inplace=True)
print(df.columns)

df=df[df["Unnamed: 4"].str.contains("TOTAL")==False]
print(df)

