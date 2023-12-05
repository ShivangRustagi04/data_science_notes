import pandas as pd 
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns= iris.feature_names)
df['target'] = iris.target
print(df.head(15))
newdf = df[df.target==2].head()
print(newdf)



































