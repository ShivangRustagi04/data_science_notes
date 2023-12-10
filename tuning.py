import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns= iris.feature_names)
df['flower'] = iris.target
df['flower'] = df['flower'].apply(lambda x : iris.target_names[x])

newdf = df[47:57]
print(newdf)



















