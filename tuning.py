import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn import svm
from sklearn.model_selection import cross_val_score
iris = load_iris()
df = pd.DataFrame(iris.data, columns= iris.feature_names)
df['flower'] = iris.target
df['flower'] = df['flower'].apply(lambda x : iris.target_names[x])

newdf = df[47:57]
print(newdf)
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(iris.data , iris.target , test_size=0.5)
model = svm.SVC(kernel='rbf',C=30,gamma='auto')
model.fit(X_train , y_train)
c = model.score(X_test, y_test)
# print(c)
b = cross_val_score(svm.SVC(kernel='linear', C=10,gamma='auto'),iris.data , iris.target , cv=5)
f = cross_val_score(svm.SVC(kernel='rbf', C=10,gamma='auto'),iris.data , iris.target , cv=5)
u = cross_val_score(svm.SVC(kernel='rbf', C=20,gamma='auto'),iris.data , iris.target , cv=5)
print(b,'\n',f,'\n',u)
kernels = ['rbf', 'linear']
C = [1,10,20]
avg_scores = {}
for kval in kernels:
    for cval in C:
        cv_scores = cross_val_score(svm.SVC(kernel=kval,C=cval,gamma='auto'),iris.data, iris.target, cv=5)
        avg_scores[kval + '_' + str(cval)] = np.average(cv_scores)
print(avg_scores )














