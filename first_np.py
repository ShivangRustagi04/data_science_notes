import numpy as np
# a = np.array([[12,6,9,6],[2,9,9,5],[3,5,8,5],[3,4,6,8]])
# print(a)
# print(a.ndim)                       TELLS DIMENSION OF ARRAY
# print(a.itemsize)
# print(a.size)                         ELEMENTS NO. OF ARRAY
# print(a.shape)
# a = np.zeros((3,4),dtype = complex  )
# print(a)
# array = np.arange(1,10,2)
# print(array)
# a = np.linspace(1,6,13)
# print(a)
# print(a.reshape(8,2))             WE CAN NORMALLY CHANGE THE N AND M OF MATRIX
# print(a.ravel())                  BASICALLY BRING ALL ELEMENT IN [1 X M] FORMAT WHERE M IS NO. OF ELEMENTS
# print(a.sum(axis = 1))            
# b = np.sqrt(a)
# print(b)
# b = np.array([[12,6,8,9],[2,9,3,6],[3,5,4,6],[3,4,7,0]])
# print(a*b)                   # BOTH ARRAY SHOULD HAVE SAME N X M 
# print(a.dot(b))

''' pandas karenge ab '''

import pandas as pd 
# df = pd.read_csv('C:\\Users\\shiva\\OneDrive\\Desktop\\practice.csv')
# print(df)
# # a = df['Data'].max()
# # print(a)
# # b = df['Series_reference'][df['STATUS']=='F'] 
# # print(b)
# # c = df['Period'].mean()
# # print("mean =",c)
# df.fillna(0,inplace=75)
# d = df['Magnitude'].mean()
# print(d)
# df = pd.read_csv('C:\\Users\\shiva\\OneDrive\\Desktop\\SHIVANG.csv')
# print(df)
# SHIVANG = {
#     'DATE' :  ['01-11-2011','02-11-2011','02-03-2011','05-03-2021','15-09-2015','31-12-2022'],
#     'TEMPERATURE' :  [30,40,23,41,7,1],
#     'EVENT' :  ['RAIN','SUNNY','WINDY','COLD','RAINY','SPRING'],
#     'DAY' :  ['MONDAY',	'TUESDAY',	'WEDNESDAY',	'THURSDAY',	'FRIDAY',	'SATURDAY']
# }
# df = pd.DataFrame(SHIVANG)
# print(df)
# rows , columns = df.shape
# print('column = ',columns)
# a = df.tail()
# print(a)
# a = df[1:6:2]
# print(a)
# b = df.shape
# print(b)
# new_df = df.fillna(0)
# print(new_df)
# new_df = df.fillna({                                   55-62 fillna command
#     'TEMPERATURE' : 10,
#     'EVENT' : "NO EVENT",
#     'DAY' : 'FRIDAY'
# })
# print(new_df)

# new_df = df.fillna(method='bfill', axis = 'columns')               # carryforward the previous value in next value which is zero...
# print(new_df)
# new_df = df.interpolate()
# print(new_df)
# new_df = df.dropna(how='all')
# print(new_df)
# new_df = df.dropna(thresh=1)
# print(new_df)

# new_df = df.replace([0.0,1.0], np.NaN)               # replace 0.0 and 1.0 by NaN
# print(new_df)

# new_df = df.replace({
#     0.0 : np.NaN,
#     'NO EVENT' : 'SEXY',
#     'NO DAY' : 'FUDDIYAN'
#     })               
# print(new_df)
# new_df = df.replace({'TEMPERATURE' : '[A-Za-z]'},'',regex=True)
# print(new_df)
# new_df = df.replace(['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY'],[0,1,2,3,4,5])                  exchanging a column value... fully
# print(new_df)

# g = df.groupby('CITY')
# print(g)
# for CITY, CITY_df in g:
#     print(CITY)                                             # categorised whole data in group of same citty name.... and will print each city data separately
#     print(CITY_df)
# a = g.get_group('MUMBAI')                                      sshows only data of mumbai
# print(a)
# a = g.max('')
# print(a)
# a = g.mean()
# print(a)
# a = g.describe()
# print(a)

# ind_weather = pd.DataFrame({
#     'city' : ['delhi','mumbai','kashmir'],
#     'temperature' : [34,45,12],
#     'humidity' : [2,4,0]
# })

# us_weather = pd.DataFrame({
#     'city' : ['california','new york','alaska'],
#     'temperature' : [34,25,42],
#     'humidity' : [1,5,2]
# })

# g = pd.concat([ind_weather,us_weather], keys = ['india','us'])             combine 2 data files together but must have same header file otherwise NaN willbe printed in second database    
# print(g)
# a = g.loc["us"]                will print only us data from concat data
# print(a)

# s = pd.Series(['humid','rain','cloudy'], name='event')
# print(s)
# df = pd.concat([us_weather,s],axis =1)
# print(df)

# d2 =  pd.DataFrame({
#     'city' : ['new york','california','san franchiso'],
#     'windspeed' : [23,45,78]
# })                                                                      # will merge two databases
# d3 = pd.merge(us_weather,d2, on = 'city', how='outer')
# print(d3)

'''mathplotlib karenge ab...'''

import matplotlib.pyplot as plt
# x = [5,5,35,35]
# y = [5,60,5,60]
# a = [5,5]
# b = [5,60]
# c = [50,5,5,50,50,30]
# d = [60,60,10,10,35,35]
# e = [50,5,5,50,50,30]
# f = [60,60,10,10,35,35]
# plt.plot(x,y,color = 'black',linewidth = 10, linestyle = 'solid')
# r = plt.show()
# print(r)
# plt.plot(a,b,color = 'black',linewidth = 10, linestyle = 'solid')
# s = plt.show()
# print(s)
# plt.plot(c,d,color = 'black',linewidth = 10, linestyle = 'solid')                                     made nigga using this
# z = plt.show()
# print(z)
# plt.plot(e,f,color = 'black',linewidth = 10, linestyle = 'solid')
# l = plt.show()
# print(l)
# x = [1,2,3,4]
# y = [23,15,67,20]
# plt.plot(x,y,'g+--')
# c = plt.show()
# print(c)

# days = [1,2,3,4,5,6,7]
# max_t = [75,80,95,85,90,100,105]
# avg_t = [7,14,35,21,28,44,42]
# min_t = [10,20,50,30,40,60,70]
# plt.xlabel('DAYS')
# plt.ylabel('TEMPERATURE')
# plt.title('WEATHER')
# plt.plot(days,max_t,label = 'MAX TEMP')
# plt.plot(days,avg_t, label = 'AVG TEMP')               BY DOING THIS 3 STATEMENT WE CAN PLOT MULTIPLE GRAPH ON XY AXIS
# plt.plot(days,min_t,label = 'MIN TEMP')

# plt.legend()
# plt.grid()
# c = plt.show()
# print(c)

#USING MATPLOTLIB WILL CREATE bargraph
# company = ['google','microsoft','amazon','meta','adobe']
# revenue = [14,15,17,18,20]
# profit = [5,6,7,8,9]
# xpos = np.arange(len(company))
# plt.xticks(xpos,company)
# plt.xlabel("FY 2022-23")
# plt.ylabel("REVENUE IN CRORE")
# plt.title("ANNUAL REPORT")
# plt.bar(xpos -0.2,revenue,width=0.4,label = 'revenue')
# plt.bar(xpos +0.2,profit, width=0.4, label = 'profit')
# plt.legend()
# a = plt.show()
# print(a)