# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 15:26:08 2016

@author: kristof
"""

import pandas as pd
import matplotlib.pyplot as plt


df= pd.read_csv("inputFile.csv", index_col=0)

df["ratio"] = df["surveys_completed"]/(df["surveys_completed"] + df["surveys_missed"])

df.to_csv("outputFile.csv")

#Separate own phones and study phones
own = df[df.own_or_study == 'own']
study = df[df.own_or_study == 'study']

#Plot histograms of in_operation and ratio from both study and own phones
plt.figure()
own["in_operation"].plot.hist()
plt.savefig('in_operation_own', format='png', bbox_inches='tight', dpi=1000)

plt.figure()
study["in_operation"].plot.hist()
plt.savefig('in_operation_study', format='png', bbox_inches='tight', dpi=1000)

plt.figure()
own["ratio"].plot.hist()
plt.savefig('survey_ratio_own', format='png', bbox_inches='tight', dpi=1000)

plt.figure()
study["ratio"].plot.hist()
plt.savefig('survey_ratio_study', format='png', bbox_inches='tight', dpi=1000)