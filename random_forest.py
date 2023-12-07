import pandas as pd
from sklearn.datasets import load_digits
digits = load_digits()
print(digits)
import matplotlib.pyplot as plt
plt.gray()
for i in range(4):
  plt.matshow(digits.images[i])
plt.show()