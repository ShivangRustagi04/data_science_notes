import pandas as pd
df = pd.read_csv("spam.csv")
a = df.head(13)
print(a)
df['spam']=df['Category'].apply(lambda x: 1 if x=='spam' else 0)
b = df.head(34)
print(b)
























































