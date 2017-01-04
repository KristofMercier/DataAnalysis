# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 11:55:19 2016

@author: discus-commander
"""
import pandas as pd
import numpy as np

path = '/home/discus-commander/Desktop/KRISTOF/Data/temp_tables/gps.csv'

df = pd.read_csv('/home/discus-commander/Desktop/KRISTOF/Data/temp_tables/gps(deltaT).csv',index_col='index')

df["record_time"] = pd.to_datetime(df["record_time"])

#Calculate the time in between entries.
df["delta_time"] = df['record_time'] - df['record_time'].shift().fillna(0)


df.to_csv('/home/discus-commander/Desktop/KRISTOF/Data/temp_tables/gps(deltaT)fix.csv')