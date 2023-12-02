import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
digits = load_digits()
a = dir(digits)
print(a)
b = digits.data[0]
print(b)
plt.gray()
for i in range(5):

    c = plt.matshow(digits.images[i])
print(c)
d = digits.target[0:5]
print(d)
X_train, X_test, y_train , y_test = train_test_split(digits.data, digits.target)
j = len(X_train)
print(j)
h = len(X_test)
print(h)

model = LogisticRegression
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data,digits.target, test_size=0.2)
model.fit(X_train, y_train)
model.score(X_test, y_test)
model.predict(digits.data[0:5])


y_predicted = model.predict(X_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test , y_predicted)
print(cm)





