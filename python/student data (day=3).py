import pandas as pd 
data={'roll no.':[10,20,30,40,50,60],
     'name':["aniket","anivesh","shravan","muskan","jai","ram"],
     'grade':['A','B','C','D','E','F']
     }
df=pd.DataFrame(data)
print(df)
print(df.head(3))
print(df.tail(2))
print(df.columns)
print(df.describe())