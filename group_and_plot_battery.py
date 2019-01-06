# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt


#df = pd.read_csv('C:\\Users\\Kristof\\Desktop\\good_data\\17-23\\dated_battery.csv')
df = pd.read_csv('/home/discus-commander/Desktop/KRISTOF/Data/temp_tables/dated_battery.csv')
df["user_id"].replace([ 763, 762, 532, 534, 764, 765, 766, 767, 769, 768, 770, 771, 772, 773, 519, 776, 777, 779, 511, 778, 780, 781, 782, 783, 784, 785, 513, 787, 786, 788, 540, 506, 516, 789, 790, 791, 792, 555, 793, 795, 794, 796, 798, 797, 799, 512, 800, 801, 802, 803, 804, 517, 806, 807, 808, 809, 551, 514, 810, 566], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], inplace=True)
df = df[df["user_id"] < 62]
del df['Unnamed: 0']
del df['index']
df = df.reset_index()
column = []


#create a table with the proper entries for dates (also encode participant ID as the year to keep all necessary information within a datetime type)
for year in range (2001,2051):   
    for day in range(17,24):
        for hour in range(0,24):
            column.append(pd.datetime(year,7,day,hour))
			        
for year in range (2052,2062):   
    for day in range(17,24):
        for hour in range(0,24):
            column.append(pd.datetime(year,7,day,hour))


df2 = pd.DataFrame()

df2["record_time"] = column

df2["record_time"] = pd.to_datetime(df2["record_time"])
df["record_time"] = pd.to_datetime(df["record_time"])

df2.set_index("record_time",inplace=True)

df2["plugged"] = pd.Series()

df2["plugged"] = 0

#set the entries of the new table to true if an occurance of the given event occured within that hour.
for index, row in df.iterrows():
    
    
    if row["plugged"] == 1 or row["plugged"] == 2:
        user_id = row["user_id"]
        if(user_id == 51):
           user_id += 1
        user_id += 2000    
        date = pd.datetime(user_id,7,row["record_time"].day,row["record_time"].hour)
        df2.xs(date)["plugged"] = 1 

df2.reset_index()

#making final table by compiling all of the calculated columns
df3 = pd.DataFrame()
column = []
for year in range (2001,2062):   
    for hour in range(0,24):
        column.append(pd.datetime(year,7,1,hour))



df3["record_time"] = column
df3["record_time"] = pd.to_datetime(df3["record_time"])

df3.set_index("record_time",inplace=True)
df3["plugged"] = pd.Series()
df3["plugged"] = 0

for index, row in df2.iterrows():
    
    
    if row["plugged"] == 1:
        date = pd.datetime(index.year,7,1,index.hour)
        df3.xs(date)["plugged"] = (df3.ix[date,0]) +1

df3.to_csv('/home/discus-commander/Desktop/KRISTOF/Data/temp_tables/battery_master.csv')


print("Success!  :)")
