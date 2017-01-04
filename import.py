# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 17:10:18 2016

@author: kristof
"""

import pandas as pd
#from lxml import etree
from sqlalchemy import create_engine, types
from tqdm import tqdm


'''
To Use, change the following five values.  You must also choose the datatypes for the uploaded data, which is below.

'''
sqlUser = ''
sqlPass = ''
path = '/home/discus-commander/Desktop/KRISTOF/discus-iepi/Ethica/original_tables/bluetooth_201609011138.csv'
#table name on server:
tableName = 'bluetooth'
#headers(can be copied from the top row of 'more' command)
headers = ["user_id","date","device_id","record_time","timestamp","dev_class","dev_name","mac","rssi"]





sqlServer = 'blinchiki.usask.ca'
sqlDatabase = 'SHED7'
appendOrReplace = 'replace'
engine = create_engine("mysql+pymysql://"+sqlUser+":"+sqlPass+"@"+sqlServer+":3306/"+sqlDatabase)
print('\nInputting Data in database...')


'''
This sends the data in chunks.
Change the datatypes of the columns below.  
Default value is a string so there is no need to change most of them.
'''
for chunk in tqdm(pd.read_csv(path, chunksize=1048576)):
    #chunk.apply(lambda x: pd.to_numeric(x, errors='ignore'))
    
    '''fix user ID's to those used by the study.'''
    chunk["user_id"].replace([ 763, 762, 532, 534, 764, 765, 766, 767, 769, 768, 770, 771, 772, 773, 519, 776, 777, 779, 511, 778, 780, 781, 782, 783, 784, 785, 513, 787, 786, 788, 540, 506, 516, 789, 790, 791, 792, 555, 793, 795, 794, 796, 798, 797, 799, 512, 800, 801, 802, 803, 804, 517, 806, 807, 808, 809, 551, 514, 810, 566], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], inplace=True)
    
    '''adding a column which indicates if the participant played pokemon.'''
    chunk["pokemon"] = False
    chunk["pokemon"][((chunk["user_id"] == 1) | (chunk["user_id"] == 2) | (chunk["user_id"] == 4) | (chunk["user_id"] == 12) | (chunk["user_id"] == 13) | (chunk["user_id"] == 17) | (chunk["user_id"] == 19) | (chunk["user_id"] == 20) | (chunk["user_id"] == 21) | (chunk["user_id"] == 26) | (chunk["user_id"] == 29) | (chunk["user_id"] == 33) | (chunk["user_id"] == 34) | (chunk["user_id"] == 36) | (chunk["user_id"] == 41) | (chunk["user_id"] == 46) | (chunk["user_id"] == 47) | (chunk["user_id"] == 48) | (chunk["user_id"] == 53) | (chunk["user_id"] == 55) | (chunk["user_id"] == 56) | (chunk["user_id"] == 61))] = True
    
    '''The following can be used if you want to calculate the delta_time between entries'''
#    chunk["record_time"] = pd.to_datetime(chunk["record_time"])
#    chunk["delta_time"] = chunk['record_time'] - chunk['record_time'].shift().fillna(0)
#    chunk["delta_time"][chunk["index"] == 0] = datetime.timedelta(microseconds=0)
    
    chunk.to_sql(tableName, engine, if_exists=appendOrReplace,
              dtype={"user_id": types.INT(),
#              "date": types.INT(),
              "record_time": types.TIMESTAMP(6),
#              "state": types.BOOLEAN(),
#              "pokemon": types.BOOLEAN(),
#              "accu": types.FLOAT(),
#              "alt": types.FLOAT(),
#              "x_axis": types.FLOAT(),
#              "y_axis": types.FLOAT(),
#               "z_axis": types.FLOAT(),
#              
#              
#              "bearing": types.FLOAT(),
#              "lat": types.FLOAT(),
#              "lon": types.FLOAT(),
#              "satellite_time": types.TIMESTAMP(6),
#              "speed": types.FLOAT()
#              "level": types.INT(),
#              "plugged": types.INT(),
#              "scale": types.INT(),
#              "status": types.INT(),
#              "temperature": types.INT(),
#              "voltage": types.INT()
              "rssi": types.INT()
    })
    appendOrReplace = 'append'


print('\nSuccess!')






















