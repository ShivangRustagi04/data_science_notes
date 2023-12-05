import pandas as pd 
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris = load_iris()
df = pd.DataFrame(iris.data, columns= iris.feature_names)
df['target'] = iris.target
print(df.head(15))
newdf = df[df.target==2].head()
print(newdf)
df0 = df[df.target==0]
df1 = df[df.target==1]
df2 = df[df.target==2]
plt.scatter(df0['sepal length (cm)'], df1['sepal width (cm)'], color='red', marker='+')
plt.scatter(df1['sepal length (cm)'], df0['sepal width (cm)'], color='green', marker='.')
plt.legend()
plt.show()


































