# -*- coding: utf-8 -*-

import pandas as pd


#This script takes input of a csv file and calculates and adds 5 new columns based on the output of a fluidsurveys survey.  
#It will calculate these values based on the 44 questions.





#change this to the input file
importFile = "inFile.csv"

#change this to the desuired output file
outputFile = "outFile.csv"

df = pd.read_csv(importFile, index_col=0)

df = df.replace("Strongly disagree", 1)
df = df.replace("Moderately disagree", 2)
df = df.replace("Neither agree nor disagree", 3)
df = df.replace("Moderately agree", 4)
df = df.replace("Strongly agree", 5)
df = df.apply(pd.to_numeric, errors='coerce')


#Do the calculations to determine the personality ratings
df["Extraversion"] = df["Has an active imagination"] + 6 - df["Is reserved"] + df["Is full of energy"] + df["Generates a lot of enthusiasm"] + 6 - df["Tends to be quiet"] + df["Has an assertive personality"] + 6 - df["Is sometimes shy, inhibited"] + df["Is outgoing and sociable"]

df["Agreeableness"] = 6 - df["Tends to find fault with others"] + df["Is helpful and unselfish with others"] + 6 - df["Starts quarrels with others"] + df["Has a forgiving nature"] + df["Is generally trusting"] + 6 - df["Can be cold and aloof"] + df["Is considerate and kind to almost everyone"] + 6 - df["Is sometimes rude to others"] + df["Likes to cooperate with others"]

df["Conscientiousness"] = df["Does a thorough job"] + 6 - df["Can be somewhat careless"] + df["Is a reliable worker"] + 6 - df["Tends to be disorganized"] + 6 - df["Tends to be lazy"] + df["Perseveres until the task is finished"] + df["Does things efficiently"] + df["Makes plans and follows through with them"] + 6 - df["Is easily distracted"]

df["Neuroticism"] = df["Is depressed, blue"] + 6 - df["Is relaxed, handles stress well"] + df["Can be tense"] + df["Worries a lot"] + 6 - df["Is emotionally stable, not easily upset"] + df["Can be moody"] + 6 - df["Remains calm in tense situations"] + df["Gets nervous easily"]

df["Openness"] = df["Is original, comes up with new ideas"] + df["Is curious about many different things"] + df["Is ingenious, a deep thinker"] + df["Has an active imagination"] + df["Is inventive"] + df["Values artistic, aesthetic experiences"] + 6 - df["Prefers work that is routine"] + df["Likes to reflect, play with ideas"] + 6 - df["Has few artistic interests"] + df["Is sophisticated in art, music, or literature"]

df2 = pd.read_csv(importFile, index_col=0)


#append the new columns to the original table and normalize them to all be between 0 and 1.
df2["Extraversion"] = (df["Extraversion"] - 8)/32
df2["Agreeableness"] = (df["Agreeableness"] - 9)/36
df2["Conscientiousness"] = (df["Conscientiousness"] - 9)/36
df2["Neuroticism"] = (df["Neuroticism"] - 8)/32
df2["Openness"] = (df["Openness"] - 10)/40


df2.to_csv(outputFile)
