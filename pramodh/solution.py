#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 01:38:47 2020

@author: wannabe-programmer
"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder



df = pd.read_csv('galaxy_data.csv') 

medimputer = SimpleImputer(missing_values=np.nan,strategy="median")

medimputer = medimputer.fit(df.iloc[:,0:5])
df.iloc[:, 0:5] = medimputer.transform(df.iloc[:, 0:5])



df['encode'] = df['Relationship_status'].map({'Single_and_stud':0.2,'Committed_inside_campus':-0.2,'Long_distance_lover': 0})
medimputer = medimputer.fit(df.iloc[:,7:8])
df.iloc[:, 7:8] = medimputer.transform(df.iloc[:, 7:8])


df = df.fillna(df['Relationship_status'].value_counts().index[0])

for i in range(df.shape[0]):
    df.iloc[i,6] = df.iloc[i,1]*0.4*0.05+df.iloc[i,2]*0.2*0.1+df.iloc[i,3]*0.1*0.2+df.iloc[i,4]*0.125*(-0.2)+df.iloc[i,7]
    df.iloc[i,6] = format(df.iloc[i,6],'.4f')

df = df.drop('encode',axis=1)

halls = [2,3,5,12]
mean_enthu = []


for i in halls:
    arr = pd.to_numeric(df[df['Hall'] == i]['Enthu'])
    mean_enthu.append(np.mean(arr))


print(halls[np.argmax(mean_enthu)])

df.to_csv("galaxy_data.csv",index = False)


