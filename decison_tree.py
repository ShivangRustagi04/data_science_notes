import pandas as pd
df = pd.read_csv("salaries.csv")
a = df.head(10)
print(a)
inputs = df.drop('salary_more_then_100k' , axis='columns')
target = ['salary_more_then_100k']
print(inputs)