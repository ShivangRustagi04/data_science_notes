from sklearn.metrics import confusion_matrix 
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
digits = load_digits()

print(digits)
import matplotlib.pyplot as plt
plt.gray()
# for i in range(4):
#   plt.matshow(digits.images[i])
# plt.show() 
df = pd.DataFrame(digits.data)
df['target'] = digits.target
X_train, X_test, y_train, y_test = train_test_split(df.drop(['target'], axis= 'columns'), digits.target ,test_size=0.1)
g = len(X_test)
# print(g)
model = RandomForestClassifier()
a = model.fit(X_train , y_train)
b = model.score(X_train,y_train)
print(b)
y_predicted = model.predict(X_test)
cm = confusion_matrix(y_test,y_predicted)
plt.figure(figsize=(90,7))
sns.heatmap(cm, annot=True)
plt.xlabel("predicted")
plt.ylabel("truth")
plt.show()





