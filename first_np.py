import numpy as np
a = np.array([[12,6,9,6],[2,9,9,5],[3,5,8,5],[3,4,6,8]])
print(a)
print(a.ndim)                       #TELLS DIMENSION OF ARRAY
print(a.itemsize)
print(a.size)                        # ELEMENTS NO. OF ARRAY
print(a.shape)
a = np.zeros((3,4),dtype = complex  )
print(a)
array = np.arange(1,10,2)
print(array)
a = np.linspace(1,6,16)
print(a)
print(a.reshape(4,4))           #  WE CAN NORMALLY CHANGE THE N AND M OF MATRIX
print(a.ravel())                 # BASICALLY BRING ALL ELEMENT IN [1 X M] FORMAT WHERE M IS NO. OF ELEMENTS            
b = np.sqrt(a)
print(b)
b = np.array([[12,6,8,9],[2,9,3,6],[3,5,4,6],[3,4,7,0]])
# print(a*b)                   # BOTH ARRAY SHOULD HAVE SAME N X M 
# print(a.dot(b))

''' pandas karenge ab '''

import pandas as pd 
df = pd.read_csv('C:\\Users\\shiva\\OneDrive\\Desktop\\DS\\practice.csv')
print(df)
a = df['Data'].max()
print(a)
b = df['Series_reference'][df['STATUS']=='F'] 
print(b)
c = df['Period'].mean()
print("mean =",c)
df = pd.read_csv('C:\\Users\\shiva\\OneDrive\\Desktop\\DS\\SHIVANG.csv')
print(df)
SHIVANG = {
    'DATE' :  ['01-11-2011','02-11-2011','02-03-2011','05-03-2021','15-09-2015','31-12-2022'],
    'TEMPERATURE' :  [30,40,23,41,7,1],
    'EVENT' :  ['RAIN','SUNNY','WINDY','COLD','RAINY','SPRING'],
    'DAY' :  ['MONDAY',	'TUESDAY',	'WEDNESDAY',	'THURSDAY',	'FRIDAY',	'SATURDAY']
}
df = pd.DataFrame(SHIVANG)
print(df)
rows , columns = df.shape
print('column = ',columns)
a = df.tail()
print(a)
a = df[1:6:2]
print(a)
b = df.shape
print(b)
new_df = df.fillna(0)
print(new_df)
new_df = df.fillna({                                  # 55-62 fillna command
    'TEMPERATURE' : 10,
    'EVENT' : "NO EVENT",
    'DAY' : 'FRIDAY'
})
print(new_df)

new_df = df.fillna(method='bfill', axis = 'columns')               # carryforward the previous value in next value which is zero...
print(new_df)
new_df = df.interpolate()
print(new_df)
new_df = df.dropna(how='all')
print(new_df)
new_df = df.dropna(thresh=1)
print(new_df)

new_df = df.replace([0.0,1.0], np.NaN)               # replace 0.0 and 1.0 by NaN
print(new_df)

new_df = df.replace({
    0.0 : np.NaN,
    'NO EVENT' : 'SEXY',
    'NO DAY' : 'FUDDIYAN'
    })               
print(new_df)
new_df = df.replace({'TEMPERATURE' : '[A-Za-z]'},'',regex=True)
print(new_df)
new_df = df.replace(['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY'],[0,1,2,3,4,5])               #   exchanging a column value... fully
print(new_df)

ind_weather = pd.DataFrame({
    'city' : ['delhi','mumbai','kashmir'],
    'temperature' : [34,45,12],
    'humidity' : [2,4,0]
})

us_weather = pd.DataFrame({
    'city' : ['california','new york','alaska'],
    'temperature' : [34,25,42],
    'humidity' : [1,5,2]
})

g = pd.concat([ind_weather,us_weather], keys = ['india','us'])           #  combine 2 data files together but must have same header file otherwise NaN willbe printed in second database    
print(g)
a = g.loc["us"]               # will print only us data from concat data
print(a)

s = pd.Series(['humid','rain','cloudy'], name='event')
print(s)
df = pd.concat([us_weather,s],axis =1)
print(df)

d2 =  pd.DataFrame({
    'city' : ['new york','california','san franchiso'],
    'windspeed' : [23,45,78]
})                                                                      # will merge two databases
d3 = pd.merge(us_weather,d2, on = 'city', how='outer')
print(d3)
