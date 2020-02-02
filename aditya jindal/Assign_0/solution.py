# -*- coding: utf-8 -*-
# Import is highly dependent on your path variables
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('galaxy_data.csv')
#filling nan values of Relationship_status column of halls according to the given condition
dataset[dataset['Hall']==5]=dataset[dataset['Hall']==5].fillna({"Relationship_status":"Commited_inside_campus"})
dataset[dataset['Hall']!=5]=dataset[dataset['Hall']!=5].fillna({"Relationship_status":"Single_and_stud"})
X=dataset.iloc[:,:].values
#importing SimpleImputer class from sklearn library to use mean function
from sklearn.impute import SimpleImputer
#creating object for the class and using strategy mean
imputer = SimpleImputer(missing_values=np.nan,
                  strategy="mean")
#creating another object to use strategy median
imputer1 = SimpleImputer(missing_values=np.nan,strategy  ="median")
#changing nan values of the dataset with mean and median 
imputer = imputer.fit(X[0:130, [1,4]])
X[0:130, [1,4]]= imputer.transform(X[0:130, [1,4]])
imputer = imputer.fit(X[130:270, [1,4]])
X[130:270, [1,4]] = imputer.transform(X[130:270, [1,4]])
imputer = imputer.fit(X[270:420, [1,4]])
X[270:420, [1,4]] = imputer.transform(X[270:420, [1,4]])
imputer = imputer.fit(X[420:500, [1,4]])
X[420:500, [1,4]] = imputer.transform(X[420:500, [1,4]])
imputer = imputer.fit(X[500:620, [1,4]])
X[500:620, [1,4]] = imputer.transform(X[500:620, [1,4]])
imputer1 = imputer1.fit(X[0:130, [2,3]])
X[0:130, [2,3]]= imputer1.transform(X[0:130, [2,3]])
imputer1 = imputer1.fit(X[130:270, [2,3]])
X[130:270, [2,3]] = imputer1.transform(X[130:270, [2,3]])
imputer1 = imputer1.fit(X[270:420, [2,3]])
X[270:420, [2,3]] = imputer1.transform(X[270:420, [2,3]])
imputer1 = imputer1.fit(X[420:500, [2,3]])
X[420:500, [2,3]] = imputer1.transform(X[420:500, [2,3]])
imputer1 = imputer1.fit(X[500:620, [2,3]])
X[500:620, [2,3]] = imputer1.transform(X[500:620, [2,3]])
#loop to calculate enthu of each student
i=0  #loop counter
while i<620 :
    if X[i,5]=="Single_and_stud":
        X[i,6]=(X[i,1]/20)*(0.4) + (X[i,2]/10)*(0.2) + (X[i,3]/10)*(0.2) + (X[i,4]/8)*(-0.2) + (0.2)
    elif X[i,5]=="Commited_inside_campus":
        X[i,-6]=(X[i,1]/20)*(0.4) + (X[i,2]/10)*(0.2) + (X[i,3]/10)*(0.2) + (X[i,4]/8)*(-0.2) - (0.2)
    else:
        X[i,6]=(X[i,1]/20)*(0.4) + (X[i,2]/10)*(0.2) + (X[i,3]/10)*(0.2) + (X[i,4]/8)*(-0.2)
    i=i+1
#converting the numpy.ndarray into dataframe
df1=pd.DataFrame(X)   
#importing statistics module
#and calculating mean of all students of respective halls
from statistics import mean
a=mean(X[0:130,6]) 
b=mean(X[130:270,6]) 
c=mean(X[270:420,6]) 
d=mean(X[420:500,6]) 
e=mean(X[500:620,6])
ar = [a,b,c,d,e]
ar1 = [2,3,5,6,12]
#checking highest enthu of a hall based on averaged enthu data of the students of the hall
f=max(a,b,c,d,e)
i=0
while i<5 :
    if ar[i]==f:
        print(ar1[i]) #printing hall with highest averaged enthu
    i=i+1
#renaming columns back to their original names after being changed to indexes on being converted to the numpy.ndarray    
df1.rename(columns = {0:'Hall',1:'Practice_hours',2:'Posts_shared',3:'Bulla_hours',4:'Classes_missed',5:'Relationship_status',6:'Enthu'},inplace=True)
export_csv = df1.to_csv (r'D:\assign 0\enthu.csv', index = None, header=True)#exporting the whole dataframe to a csv file