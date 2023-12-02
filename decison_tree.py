import pandas as pd
df = pd.read_csv("salaries.csv")
a = df.head(10)
print(a)
inputs = df.drop('salary_more_then_100k' , axis='columns')
target = ['salary_more_then_100k']
print(inputs)
from sklearn.preprocessing import LabelEncoder
le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()
inputs['company_n'] = le_company.fit_transform(inputs['company'])

inputs['job_n'] = le_company.fit_transform(inputs['job'])

inputs['degree_n'] = le_company.fit_transform(inputs['degree'])
f = inputs.head(19)
print(f)
inputs_n = inputs.drop(['company','job','degree'],axis='columns')
print(inputs_n)
