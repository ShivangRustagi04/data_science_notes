from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import KFold
kf = KFold(n_splits=3)
folds = StratifiedKFold(n_splits=3)
digits = load_digits()
X_train , X_test , y_train , y_test = train_test_split(digits.data, digits.target, test_size=0.1)
# lr = LogisticRegression()
# lr.fit(X_train,y_train)
# a = lr.score(X_test,y_test)
# print(a)
# svm = SVC()
# svm.fit(X_train,y_train)
# b = svm.score(X_test,y_test)
# print(b)
# rf = RandomForestClassifier()
# rf.fit(X_train,y_train)
# c = rf.score(X_test,y_test)
# print(c)
def get_score(model, X_train , X_test , y_train , y_test):
    model.fit(X_train, y_train)
    return model.score(X_test,y_test)
scores_1 = []
scores_svm = []
scores_rf = []

for train_index , test_index in kf.split(digits.data):
    X_train,X_test,y_train,y_test = digits.data[train_index], digits.data[test_index], \
                                    digits.target[train_index], digits.target[test_index]
    scores_1.append(get_score(LogisticRegression(), X_train,X_test, y_train, y_test))
    scores_svm.append(get_score(SVC(), X_train,X_test, y_train, y_test))
    scores_rf.append(get_score(RandomForestClassifier(), X_train,X_test, y_train, y_test))

print(scores_1)
print(scores_svm)
print(scores_rf)











