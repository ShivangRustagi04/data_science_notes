import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
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










