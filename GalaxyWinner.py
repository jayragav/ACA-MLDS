# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:06:14 2020

@author: sanja
"""

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import csv
dataset = pd.read_csv('galaxy_data.csv')
X= dataset.iloc[:270,:].values 
imputer=SimpleImputer(missing_values=np.nan,
                        strategy="constant")
imputer1 = SimpleImputer(missing_values=np.nan,
                        strategy="mean")
imputer2 = SimpleImputer(missing_values=np.nan,
                  strategy="median")
imputer1= imputer1.fit(X[:,1:2])
X[:,1:2] = imputer1.transform(X[:,1:2])
imputer1= imputer1.fit(X[:,4:5])
X[:,4:5] = imputer1.transform(X[:,4:5])
imputer2= imputer2.fit(X[:,2:4])
X[:,2:4]= imputer2.transform(X[:,2:4])
imputer= imputer.fit(X[:,5:6])
X[:,5:6] = imputer.transform(X[:,5:6])
for i in X[:,5:6]:
    if i[0]=='missing_value':
        i[0]='Single_and_stud'
X1= dataset.iloc[270:420,:].values
imputer1= imputer1.fit(X1[:,1:2])
X1[:,1:2] = imputer1.transform(X1[:,1:2])
imputer1= imputer1.fit(X[:,4:5])
X1[:,4:5] = imputer1.transform(X1[:,4:5])
imputer2= imputer2.fit(X1[:,2:4])
X1[:,2:4]= imputer2.transform(X1[:,2:4])
imputer= imputer.fit(X1[:,5:6])
X1[:,5:6] = imputer.transform(X1[:,5:6])
for i in X1[:,5:6]:
    if i[0]=='missing_value':
        i[0]='Committed_inside_campus'
X2= dataset.iloc[420:620,:].values 
imputer1= imputer1.fit(X2[:,1:2])
X2[:,1:2] = imputer1.transform(X2[:,1:2])
imputer1= imputer1.fit(X2[:,4:5])
X2[:,4:5] = imputer1.transform(X2[:,4:5])
imputer2= imputer2.fit(X2[:,2:4])
X2[:,2:4]= imputer2.transform(X2[:,2:4])
imputer= imputer.fit(X2[:,5:6])
X2[:,5:6] = imputer.transform(X2[:,5:6])
for i in X2[:,5:6]:
    if i[0]=='missing_value':
        i[0]='Single_and_stud'
dataset.iloc[:270,:]=X[:,:]
dataset.iloc[270:420,:]=X1[:,:]
dataset.iloc[420:,:]=X2[:,:]
Enth=[]
for j in range(620):
    if dataset['Relationship_status'][j]== 'Single_and_stud':
         E=(((dataset['Practice_hours'][j]+dataset['Bulla_hours'][j]+dataset['Posts_shared'][j])*0.2)/10)-((dataset['Classes_missed'][j]*0.2)/8)+0.2
         Enth.append(E)
    elif dataset['Relationship_status'][j]== 'Long_distance_lover':
         E=(((dataset['Practice_hours'][j]+dataset['Bulla_hours'][j]+dataset['Posts_shared'][j])*0.2)/10)-((dataset['Classes_missed'][j]*0.2)/8)
         Enth.append(E)
    elif dataset['Relationship_status'][j]== 'Committed_inside_campus':
         E=(((dataset['Practice_hours'][j]+dataset['Posts_shared'][j]+dataset['Bulla_hours'][j])*0.2)/10)-((dataset['Classes_missed'][j]*0.2)/8)-0.2
         Enth.append(E)
avg_enthu=[]
a2=sum((Enth[:130]))/130
avg_enthu.append(sum((Enth[:130]))/130)
win=a2
a3=sum((Enth[130:270]))/140
avg_enthu.append(sum((Enth[130:270]))/140)
if a3>win :win=a3
a5=sum((Enth[270:420]))/150
avg_enthu.append(sum((Enth[270:420]))/150)
if a5>win :win=a5
a6=sum((Enth[420:500]))/80
avg_enthu.append(sum((Enth[420:500]))/80)
if a6>win :win=a6
a12=sum((Enth[500:620]))/120
avg_enthu.append(sum((Enth[500:620]))/120)
if a12>win :win=a12
if win==a2 :print("Hall2")
if win==a3 :print("Hall3")
if win==a5 :print("Hall5")
if win==a6 :print("Hall6")
if win==a12:print("Hall12")
with open('enthu.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["Enth"])
    for i in range(620):
        writer.writerow([Enth[i]])

