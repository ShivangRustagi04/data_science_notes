
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
data=pd.read_csv("C:\\Users\\shiva\\OneDrive\\Desktop\\CodSoft\\tested.csv")
print(data)
a = data.shape
print(a)
b = data.info()
print(b)
c = data.isnull().sum()
print(c)
data=data.drop(columns='Cabin',axis=1)
data['Age'].fillna(data['Age'].mean(),inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0],inplace=True)
data['Fare'].fillna(data['Fare'].mode()[0],inplace=True)
data.isnull().sum().sum()
data['Survived'].value_counts()
data.describe()
sns.set()
n = sns.countplot(x='Survived',data=data)
print(n)
m = sns.countplot(x='Sex',data=data)
print(m)
u = sns.countplot(x='Sex',hue='Survived',data=data)
print(u)
g = sns.countplot(x='Pclass',data=data)
print(g)
sns.countplot(x='Pclass',hue='Survived',data=data)
data['Sex'].value_counts()
data['Embarked'].value_counts()
data.replace({'Sex':{'male':0,'female':1},'Embarked':{'S':0,'C':1,'Q':2}},inplace=True)
print(data)
X=data.drop(columns=['PassengerId','Name','Ticket'],axis=1)
Y=data['Survived']
print(X)
print(Y)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=2)
print(X.shape,X_train.shape,X_test.shape)
model=LogisticRegression()
model.fit(X_train,Y_train)
X_train_prediction=model.predict(X_train)
print(X_train_prediction)
train_data_accuracy=accuracy_score(Y_train,X_train_prediction)
print("Accuracy Score of training data: ",train_data_accuracy)
X_test_prediction=model.predict(X_test)
print(X_test_prediction)
test_data_accuracy=accuracy_score(Y_test,X_test_prediction)
print("Accuracy score of testing data:",test_data_accuracy)
plt.figure(figsize=(8, 6))
sns.histplot(data=data, x='Age', bins=30, kde=True)
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Count')
v = plt.show()
print(v)
sns.pairplot(data=data, hue='Survived', diag_kind='kde')
gr = plt.show()
print(gr)
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
hh = plt.show()
print(hh)
sns.barplot(x='Pclass', y='Survived', data=data)
plt.title('Survival Rate by Passenger Class')
bb = plt.show()
print(bb)
sns.barplot(x='Sex', y='Survived', data=data)
plt.title('aSurvival Rate by Gender')
nn = plt.show()
print(nn)
sns.countplot(x='Embarked', hue='Survived', data=data)
plt.title('Survival by Port of Embarkation')
gg = plt.show()
print(gg)
model = GaussianNB()
n = model.score(X_test,Y_test)
print(n)











