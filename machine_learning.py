import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import pickle
import joblib
from sklearn.linear_model import LinearRegression 
df = pd.read_csv('C:\\Users\\shiva\\OneDrive\\Desktop\\DS\\SHIVANG.csv')
print(df)

# plt.xlabel('area')
# plt.ylabel('price')
# plt.scatter(df['area'],df['price'], color = 'red', marker='+')
# plt.show()
# # linear regression in single variable
# reg = linear_model.LinearRegression()
# reg.fit(df[['area']],df.price)
# # y = mx + c
# a = reg.predict([[2800]])
# print(a)                                      # tells x
# b = reg.intercept_
# print(b)                                        # tells c
# c = reg.coef_
# print(c)                                    # tells m
# print(83.78378378*2800 + 337297.2972972974 )
# d = pd.read_csv('C:\\Users\\shiva\\OneDrive\\Desktop\\DS\\areas.csv')
# print(d)
# e = reg.predict(d)                        # 21-27 homework question to predict price in following year
# print(e)
# d['prices'] = e
# d.to_csv('C:\\Users\\shiva\\OneDrive\\Desktop\\DS\\sagar.csv',index=False)
# plt.xlabel('area')
# plt.ylabel('price')
# plt.scatter(df.area,df.price, color = 'red', marker='+')
# plt.plot(df.area,reg.predict(df[['area']]),color = 'blue')          # draw graph and tells whether price is low or up
# plt.show()

# #linear regression in multiple variables

# d = pd.read_csv('C:\\Users\\shiva\\OneDrive\\Desktop\\DS\\question.csv')
# print(d)
# import math
# median_bedrooms = math.floor(d.bedroom.median())
# print('median = ' ,median_bedrooms)
# d.bedroom = d.bedroom.fillna(median_bedrooms)
# print(d)
# reg = linear_model.LinearRegression()
# reg.fit(d[['area','bedroom','age']],d.price)
# a = reg.coef_
# print('coff=',a)
# b = reg.intercept_
# print('inter=' ,b)
# c = reg.predict([[2500,4,5]])
# print('predict',c)
# print(-166.5810369*3000 + 48101.86219361 * 3 + -940.7428467*40 +1015256.5846922402)
# from sklearn.datasets import load_digits
# digits = load_digits()
# print (dir(digits))
# print(digits.data[0])
# plt.gray()
# a = plt.matshow(digits.images[0])
# a = plt.matshow(digits.images[0])
# def gradient_descent(x,y):
#     m_curr = b_curr = 0
#     iterations = 1000
#     n = len(x)
#     learning_rate = 0.001
#     for i in range(iterations):
#         y_predicted = m_curr * x + b_curr
#         cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
#         md = -(2/n) * sum(x*(y-y_predicted))
#         bd = -(2/n) * sum(y-y_predicted)
#         m_curr - m_curr - learning_rate * md
#         b_curr = b_curr - learning_rate * bd
#         print ("m {}, b {} ,cost {} iteration {}".format(m_curr,b_curr,cost,i))

# x = np.array([1,2,3,4,5])
# y = np.array([5,7,9,11,13])

# gradient_descent(x,y)
# with open('reg_pickle','wb') as f:
#     pickle.dump(reg,f)
# with open('reg_pickle','rb') as f:
#     mp = pickle.load(f)
# c = mp.predict([[5000]])
# print(c)
# joblib.dump(reg,'reg_joblib')
# mj = joblib.load('reg_joblib')
# a = mj.predict([[5000]])
# print(a)
pf = pd.read_csv("carprices.csv") 
print(pf)
i = pd.get_dummies(pf.Car_Model)
print(i) 
merged = pd.concat([pf,i],axis = 'columns')
print(merged)
final = merged.drop(['Car_Model','Mercedez Benz C class'], axis = 'columns')
print(final)
model = LinearRegression()
x = final.drop('Sell_Price',axis='columns')
print(x)
y = final['Sell_Price']
print(y)
model.fit(x,y)
p = model.predict([[86000,7,0,1]])
print(p)
ab = model.score(x,y)
print(ab)
