import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
df = pd.read_csv("salaries.csv")
a = df.head(10)
print(a)
print("Column names:", df.columns)
target_column_name = 'salary_more_then_100k'
inputs = df.drop(target_column_name, axis='columns')
target = df[target_column_name]
le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_job.fit_transform(inputs['job'])
inputs['degree_n'] = le_degree.fit_transform(inputs['degree'])
f = inputs.head(10)
print(f)
inputs_n = inputs.drop(['company', 'job', 'degree'], axis='columns')
print(inputs_n)
X_train, X_test, y_train, y_test = train_test_split(inputs_n, target, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
train_accuracy = model.score(X_train, y_train)
print("Training Accuracy:", train_accuracy)
test_accuracy = model.score(X_test, y_test)
print("Testing Accuracy:", test_accuracy)
