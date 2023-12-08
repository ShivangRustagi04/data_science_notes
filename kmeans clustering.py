from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
df = pd.read_csv("income.csv")
a = plt.scatter(df['Age'],df['Income($)'])
plt.show()
km = KMeans(n_clusters=3)












