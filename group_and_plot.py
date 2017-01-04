# -*- coding: utf-8 -*-
"""
Spyder Editor

This script will create a table which indicates 
whether or not a phone was plugged in during each hour of the day.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('C:\\Users\\Kristof\\Desktop\\good_data\\17-23\\dated_battery.csv')

df = df.reset_index()
column = []

#create a table with the proper entries for dates (also encode participant ID as the year to keep all necessary information within a datetime type)
for year in range (2001,2061):   
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
    if(row["plugged"] == 1):
        user_id = row["user_id"]
        if(user_id > 50):
            user_id -= 1
        user_id += 2000    
        date = pd.datetime(user_id,7,row["record_time"].day,row["record_time"].hour)
        df2.xs(date)["plugged"] = 1 
        

df2.to_csv('C:\\Users\\Kristof\\Desktop\\good_data\\17-23\\battery_master.csv')
print("Success!  :)")