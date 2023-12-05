# import pandas as pd 
# from sklearn.datasets import load_iris
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC
# from sklearn.datasets import load_digits
# a = load_digits()
# print(a)

# df = pd.DataFrame(a.data, columns= a.feature_names)
# df['target'] = a.target
# print(df.head(15))
# newdf = df[df.target==2].head()
# print(newdf)
# df0 = df[df.target==0]
# df1 = df[df.target==1]
# df2 = df[df.target==2]
# plt.scatter(df0['pixel_0_2'], df1['pixel_7_5'], color='red', marker='+')
# plt.scatter(df1['pixel_7_5'], df0['pixel_0_2'], color='green', marker='.')
# plt.show()
# X = df.drop({'target', 'pixel_0_2'}, axis= 'columns')
# y = df.target
# X_train, X_test, y_train, y_test = train_test_split(df.drop('target',axis='columns'), df.target, test_size=0.3)
# model = SVC()
# model.fit(X_test, y_test) 
# g = model.score(X_test, y_test)
# print(g)
import pandas as pd 
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load digits dataset
a = load_digits()
df = pd.DataFrame(a.data, columns=a.feature_names)
df['target'] = a.target

# Scatter plot
df0 = df[df.target == 0]
df1 = df[df.target == 1]
plt.scatter(df0['pixel_0_2'], df0['pixel_7_5'], color='red', marker='+', label='Digit 0')
plt.scatter(df1['pixel_0_2'], df1['pixel_7_5'], color='green', marker='.', label='Digit 1')
plt.xlabel('pixel_0_2')
plt.ylabel('pixel_7_5')
plt.legend()
plt.show()

# Split the data into training and test sets
X = df.drop(['target', 'pixel_0_2'], axis='columns')
y = df.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the SVM model
model = SVC()
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print(f'Model Accuracy: {accuracy * 100:.2f}%')






























