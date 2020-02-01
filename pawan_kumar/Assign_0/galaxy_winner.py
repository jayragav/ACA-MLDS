#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:45:46 2020

@author: pawan
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
import csv
import numpy as np
from random import randint
H5_STRENGTH = 150
H2_STRENGTH = 130
H3_STRENGTH = 140
H12_STRENGTH = 120
H6_STRENGTH = 80

enthu=[]
import numpy as np
df=pd.read_csv('galaxy_data.csv')
df.head()
x=df.iloc[:130,:].values
imputer = SimpleImputer(missing_values=np.NaN, strategy="mean")
imputer2 = SimpleImputer(missing_values=np.nan, strategy='median')
imputer3 = SimpleImputer(missing_values=np.NaN, strategy="constant")
imputer = imputer.fit(x[:,1:2])
x[:, 1:2] = imputer.transform(x[:, 1:2])
imputer = imputer.fit(x[:,4:5])
x[:,4:5] = imputer.transform(x[:,4:5])
imputer2 = imputer2.fit(x[:,2:4])
x[:,2:4] = imputer2.transform(x[:,2:4])
imputer3 = imputer3.fit(x[:,5:6])
x[:,5:6] = imputer3.transform(x[:,5:6])
for i in x[:,5:6]:
    if i[0]=='missing_value':
        i[0]='Single_and_stud'
x1=df.iloc[130:270,:].values
imputer = imputer.fit(x1[:,1:2])
x1[:, 1:2] = imputer.transform(x1[:, 1:2])
imputer = imputer.fit(x1[:,4:5])
x1[:,4:5] = imputer.transform(x1[:,4:5])
imputer2 = imputer2.fit(x1[:,2:4])
x1[:,2:4] = imputer2.transform(x1[:,2:4])
imputer3 = imputer3.fit(x1[:,5:6])
x1[:,5:6] = imputer3.transform(x1[:,5:6])
for i in x1[:,5:6]:
    if i[0]=='missing_value':
        i[0]='Single_and_stud'
x2=df.iloc[270:420,:].values
imputer = imputer.fit(x2[:,1:2])
x2[:, 1:2] = imputer.transform(x2[:, 1:2])
imputer = imputer.fit(x2[:,4:5])
x2[:,4:5] = imputer.transform(x2[:,4:5])
imputer2 = imputer2.fit(x2[:,2:4])
x2[:,2:4] = imputer2.transform(x2[:,2:4])
imputer3 = imputer3.fit(x2[:,5:6])
x2[:,5:6] = imputer3.transform(x2[:,5:6])
for i in x2[:,5:6]:
    if i[0]=='missing_value':
        i[0]='Committed_inside_campus'
x3=df.iloc[420:500,:].values
imputer = imputer.fit(x3[:,1:2])
x3[:, 1:2] = imputer.transform(x3[:, 1:2])
imputer = imputer.fit(x3[:,4:5])
x3[:,4:5] = imputer.transform(x3[:,4:5])
imputer2 = imputer2.fit(x3[:,2:4])
x3[:,2:4] = imputer2.transform(x3[:,2:4])
imputer3 = imputer3.fit(x3[:,5:6])
x3[:,5:6] = imputer3.transform(x3[:,5:6])
for i in x3[:,5:6]:
    if i[0]=='missing_value':
        i[0]='Single_and_stud'
x4=df.iloc[500:,:].values
imputer = imputer.fit(x4[:,1:2])
x4[:, 1:2] = imputer.transform(x4[:, 1:2])
imputer = imputer.fit(x4[:,4:5])
x4[:,4:5] = imputer.transform(x4[:,4:5])
imputer2 = imputer2.fit(x4[:,2:4])
x4[:,2:4] = imputer2.transform(x4[:,2:4])
imputer3 = imputer3.fit(x4[:,5:6])
x4[:,5:6] = imputer3.transform(x4[:,5:6])
for i in x4[:,5:6]:
    if i[0]=='missing_value':
        i[0]='Single_and_stud'
df.iloc[:130,:]=x[:,:]
df.iloc[130:270,:]=x1[:,:]
df.iloc[270:420,:]=x2[:,:]
df.iloc[420:500,:]=x3[:,:]
df.iloc[500:,:]=x4[:,:]

for i in range(620):
    if df['Relationship_status'][i]== 'Single_and_stud':
         enth=(((df['Practice_hours'][i]+df['Posts_shared'][i]+df['Bulla_hours'][i])*0.2)/10)-((df['Classes_missed'][i]*0.2)/8)+0.2
         enthu.append(enth)
    elif df['Relationship_status'][i]== 'Committed_inside_campus':
         enth=(((df['Practice_hours'][i]+df['Posts_shared'][i]+df['Bulla_hours'][i])*0.2)/10)-((df['Classes_missed'][i]*0.2)/8)-0.2
         enthu.append(enth)
    elif df['Relationship_status'][i]== 'Long_distance_lover':
         enth=(((df['Practice_hours'][i]+df['Posts_shared'][i]+df['Bulla_hours'][i])*0.2)/10)-((df['Classes_missed'][i]*0.2)/8)
         enthu.append(enth)

with open('enthu_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Enthu"])
    for i in range(620):
        writer.writerow([enthu[i]])
avg=[]
avg2=sum(enthu[:130])/130
avg3=sum(enthu[130:270])/140
avg5=sum(enthu[270:420])/150
avg6=sum(enthu[420:500])/80
avg12=sum(enthu[500:620])/120
avg.append(avg2)
avg.append(avg3)
avg.append(avg5)
avg.append(avg6)
avg.append(avg12)
high=max(avg)
print("THE GALAXY 2020 WINNER IS:")
if avg2==high: print("hall2")
elif avg3==high: print("hall3")
elif avg5==high: print("hall5")
elif avg6==high: print("hall6")
elif avg12==high: print("hall12")


        
print("done")