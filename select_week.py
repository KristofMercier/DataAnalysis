# -*- coding: utf-8 -*-
"""
Spyder Editor

Selects a week from a table
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


cols ={"index","user_id","record_time","pokemon","delta_time"}

df = pd.read_csv("gps_delta_time.csv",dtype={"index": "int","user_id": "int","record_time": "str","pokemon": "int","delta_time": "str"},usecols=cols)

df = df[(df['record_time'] >= '2016-07-17') & (df['record_time'] < '2016-07-24')]

df = df.reset_index()

''' 
times = pd.DatetimeIndex(df.record_time)
grouped = df.groupby([times.hour, times.minute])
'''
df.to_csv("datedGps.csv")



