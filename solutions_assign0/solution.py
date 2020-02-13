# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

dataset = pd.read_csv('galaxy_data.csv')


h2 = dataset.loc[dataset["Hall"]==2]
h3 = dataset.loc[dataset["Hall"]==3]
h5 = dataset.loc[dataset["Hall"]==5]
h6 = dataset.loc[dataset["Hall"]==6]
h12 = dataset.loc[dataset["Hall"]==12]


#storing the strength of each hall
h2_l = len(h2)
h3_l = len(h3)
h5_l = len(h5)
h6_l = len(h6)
h12_l = len(h12)

from sklearn.impute import SimpleImputer

#imputers for various cases
imputer1 = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer2 = SimpleImputer(missing_values=np.nan, strategy='median')
imputer3 = SimpleImputer(missing_values=np.nan, strategy="constant", fill_value="Single_and_stud")
imputer4 = SimpleImputer(missing_values=np.nan, strategy="constant",fill_value="Committed_inside_campus")


#converting into numpy array
x1 = h2.iloc[:,:].values
x2 = h3.iloc[:,:].values
x3 = h5.iloc[:,:].values
x4 = h6.iloc[:,:].values
x5 = h12.iloc[:,:].values




# filling the missing values
x1[:,1:2] = imputer1.fit_transform(x1[:,1:2])
x2[:,1:2] = imputer1.fit_transform(x2[:,1:2])
x3[:,1:2] = imputer1.fit_transform(x3[:,1:2])
x4[:,1:2] = imputer1.fit_transform(x4[:,1:2])
x5[:,1:2] = imputer1.fit_transform(x5[:,1:2])

x1[:,2:4] = imputer2.fit_transform(x1[:,2:4])
x2[:,2:4] = imputer2.fit_transform(x2[:,2:4])
x3[:,2:4] = imputer2.fit_transform(x3[:,2:4])
x4[:,2:4] = imputer2.fit_transform(x4[:,2:4])
x5[:,2:4] = imputer2.fit_transform(x5[:,2:4])

x1[:,4:5] = imputer1.fit_transform(x1[:,4:5])
x2[:,4:5] = imputer1.fit_transform(x2[:,4:5])
x3[:,4:5] = imputer1.fit_transform(x3[:,4:5])
x4[:,4:5] = imputer1.fit_transform(x4[:,4:5])
x5[:,4:5] = imputer1.fit_transform(x5[:,4:5])


x1[:,5:6] = imputer3.fit_transform(x1[:,5:6])
x2[:,5:6] = imputer4.fit_transform(x2[:,5:6])
x3[:,5:6] = imputer3.fit_transform(x3[:,5:6])
x4[:,5:6] = imputer3.fit_transform(x4[:,5:6])
x5[:,5:6] = imputer3.fit_transform(x5[:,5:6])



#copying the results to the original dataset 
h2.loc[:,:] = x1
h3.loc[:,:] = x2
h5.loc[:,:] = x3
h6.loc[:,:] = x4
h12.loc[:,:] = x5


#computing enthu 

enth_2 =[]
for i in range(h2_l):
    if   h2['Relationship_status'][i]== 'Single_and_stud':
        e_f = 0.2
    elif h2['Relationship_status'][i]== 'Committed_inside_campus':
        e_f =-0.2
    elif h2['Relationship_status'][i]== 'Long_distance_lover':
        e_f = 0
        
    enth=(((h2['Practice_hours'][i]+h2['Posts_shared'][i]+h2['Bulla_hours'][i])*0.2)/10)-((h2['Classes_missed'][i]*0.2)/8)+ e_f
    enth_2.append(enth)


enth_3 =[]
for i in range(h2_l,h2_l+ h3_l):
    if   h3['Relationship_status'][i]== 'Single_and_stud':
        e_f = 0.2
    elif h3['Relationship_status'][i]== 'Committed_inside_campus':
        e_f =-0.2
    elif h3['Relationship_status'][i]== 'Long_distance_lover':
        e_f = 0
        
    enth=(((h3['Practice_hours'][i]+h3['Posts_shared'][i]+h3['Bulla_hours'][i])*0.2)/10)-((h3['Classes_missed'][i]*0.2)/8)+ e_f
    enth_3.append(enth)


enth_5 =[]
for i in range(h2_l+ h3_l,h2_l+h3_l+ h5_l):
    if   h5['Relationship_status'][i]== 'Single_and_stud':
        e_f = 0.2
    elif h5['Relationship_status'][i]== 'Committed_inside_campus':
        e_f =-0.2
    elif h5['Relationship_status'][i]== 'Long_distance_lover':
        e_f = 0
        
    enth=(((h5['Practice_hours'][i]+h5['Posts_shared'][i]+h5['Bulla_hours'][i])*0.2)/10)-((h5['Classes_missed'][i]*0.2)/8)+ e_f
    enth_5.append(enth)


enth_6 =[]
for i in range(h2_l+h3_l+ h5_l,h2_l+h3_l+ h5_l+ h6_l):
    if   h6['Relationship_status'][i]== 'Single_and_stud':
        e_f = 0.2
    elif h6['Relationship_status'][i]== 'Committed_inside_campus':
        e_f =-0.2
    elif h6['Relationship_status'][i]== 'Long_distance_lover':
        e_f = 0
        
    enth=(((h6['Practice_hours'][i]+h6['Posts_shared'][i]+h6['Bulla_hours'][i])*0.2)/10)-((h6['Classes_missed'][i]*0.2)/8)+ e_f
    enth_6.append(enth)


enth_12 =[]
for i in range(h2_l+h3_l+ h5_l+ h6_l,h2_l+h3_l+ h5_l+h6_l+h12_l):
    if   h12['Relationship_status'][i]== 'Single_and_stud':
        e_f = 0.2
    elif h12['Relationship_status'][i]== 'Committed_inside_campus':
        e_f =-0.2
    elif h12['Relationship_status'][i]== 'Long_distance_lover':
        e_f = 0
        
    enth=(((h12['Practice_hours'][i]+h12['Posts_shared'][i]+h12['Bulla_hours'][i])*0.2)/10)-((h12['Classes_missed'][i]*0.2)/8)+ e_f
    enth_12.append(enth)



#final array 
enthu = enth_2 + enth_3 +enth_5 + enth_6 + enth_12


#writing into csv file
with open('enthu.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Enthu"])
    for i in range(len(dataset)):
        writer.writerow([enthu[i]])


#computing averages of halls
av_2 = sum(enth_2)/h2_l
av_3 = sum(enth_3)/h3_l
av_5 = sum(enth_5)/h5_l
av_6 = sum(enth_6)/h6_l
av_12 = sum(enth_12)/h12_l

max_av = max(av_2,av_3,av_5,av_6,av_12)



#printing the winner
switcher = { 
	av_2: "Hall 2 is the winner", 
        av_3: "Hall 3 is the winner", 
        av_5: "Hall 5 is the winner", 
        av_6: "Hall 6 is the winner", 
        av_12: "Hall 12 is the winner", 
} 
    

print(switcher.get(max_av))



