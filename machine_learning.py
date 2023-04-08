import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
# df = pd.read_csv('C:\\Users\\shiva\\OneDrive\\Desktop\\SHIVANG.csv')
# print(df)
# plt.xlabel('area')
# plt.ylabel('price')
# plt.scatter(df.area,df.price, color = 'red', marker='+')
# # # plt.show()
#linear regression in single variable
# reg = linear_model.LinearRegression()
# reg.fit(df[['year']],df.price)
# y = mx + c
# a = reg.predict([[2800]])
# print(a)                                       tells x
# b = reg.intercept_
# print(b)                                         tells c
# c = reg.coef_
# print(c)                                     tells m
# print(83.78378378*2800 + 337297.2972972974 )
# d = pd.read_csv('C:\\Users\\shiva\\OneDrive\\Desktop\\question.csv')
# print(d)
# e = reg.predict(d)                         21-27 homework question to predict price in following year
# print(e)
# d['prices'] = e
# print(d)
# d.to_csv('C:\\Users\\shiva\\OneDrive\\Desktop\\sagar.csv',index=False)
# plt.xlabel('area')
# plt.ylabel('price')
# plt.scatter(df.area,df.price, color = 'red', marker='+')
# plt.plot(df.area,reg.predict(df[['area']]),color = 'blue')           draw graph and tells whether price is low or up
# plt.show()

#linear regression in multiple variables

d = pd.read_csv('C:\\Users\\shiva\\OneDrive\\Desktop\\question.csv')
print(d)
import math
median_bedrooms = math.floor(d.bedroom.median())
print('median = ' ,median_bedrooms)
d.bedroom = d.bedroom.fillna(median_bedrooms)
print(d)


