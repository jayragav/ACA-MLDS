# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:45:49 2020

@author: Amit
"""
import csv
import pandas as pd
dataset = pd.read_csv('galaxy_data.csv')
hall = dataset.iloc[:,0]
practice_hours = dataset.iloc[:,1]
post_shared = dataset.iloc[:,2]
bulla_hours = dataset.iloc[:,3]
classes_missed = dataset.iloc[:,4]
r_status = dataset.iloc[:,5]
hall2_empty = 0
hall2_total = 0
hall5_empty = 0
hall5_total = 0
hall12_empty = 0
hall12_total = 0
hall3_empty = 0
hall3_total = 0
hall6_empty = 0
hall6_total = 0
count = 0
for i in hall:
    if(i==2):
        hall2_total+=1
        if(pd.isna(practice_hours[count])): hall2_empty+=1
    if(i==3):
        hall3_total+=1
        if(pd.isna(practice_hours[count])): hall3_empty+=1
    if(i==12):
        hall12_total+=1
        if(pd.isna(practice_hours[count])): hall12_empty+=1
    if(i==5):
        hall5_total+=1
        if(pd.isna(practice_hours[count])): hall5_empty+=1
    if(i==6):
        hall6_total+=1
        if(pd.isna(practice_hours[count])): hall6_empty+=1
    count+=1
hall2_data = dataset.iloc[0:hall2_total,:]
hall3_data = dataset.iloc[hall2_total:(hall2_total+hall3_total),:]
hall5_data = dataset.iloc[(hall2_total+hall3_total):(hall2_total+hall3_total+hall5_total),:]
hall6_data = dataset.iloc[(hall2_total+hall3_total+hall5_total):(hall6_total+hall2_total+hall3_total+hall5_total),:]
hall12_data = dataset.iloc[(hall6_total+hall2_total+hall3_total+hall5_total):(hall12_total+hall6_total+hall2_total+hall3_total+hall5_total),:]
total_practice = 0
total_mic = 0
#mean for hall2
for i in range(hall2_empty):
    for j in range(hall2_total):
        if(not pd.isna(hall2_data.iloc[j,1])):
            total_practice+=hall2_data.iloc[j,1]
            total_mic+=hall2_data.iloc[j,4]
    for j in range(hall2_total):
        if(pd.isna(hall2_data.iloc[j,1])):
            hall2_data.loc[j,"Practice_hours"] = total_practice/(hall2_total-hall2_empty+i)
            hall2_data.loc[j,"Classes_missed"] = total_mic/(hall2_total-hall2_empty+i)
            break
    total_practice=0
    total_mic = 0
#mean for hall3
for i in range(hall3_empty):
    for j in range(hall3_total):
        if(not pd.isna(hall3_data.iloc[j,1])):
            total_practice+=hall3_data.iloc[j,1]
            total_mic+=hall3_data.iloc[j,4]
    for j in range(hall3_total):
        if(pd.isna(hall3_data.iloc[j,1])):
            hall3_data.loc[j+hall2_total,"Practice_hours"] = total_practice/(hall3_total-hall3_empty+i)
            hall3_data.loc[j+hall2_total,"Classes_missed"] = total_mic/(hall3_total-hall3_empty+i)
            break
    total_practice=0
    total_mic = 0
#mean for hall5
for i in range(hall5_empty):
    for j in range(hall5_total):
        if(not pd.isna(hall5_data.iloc[j,1])):
            total_practice+=hall5_data.iloc[j,1]
            total_mic+=hall5_data.iloc[j,4]
    for j in range(hall5_total):
        if(pd.isna(hall5_data.iloc[j,1])):
            hall5_data.loc[j+hall2_total+hall3_total,"Practice_hours"] = total_practice/(hall5_total-hall5_empty+i)
            hall5_data.loc[j+hall2_total+hall3_total,"Classes_missed"] = total_mic/(hall5_total-hall5_empty+i)
            break
    total_practice=0
    total_mic = 0
#mean for hall6
for i in range(hall6_empty):
    for j in range(hall6_total):
        if(not pd.isna(hall6_data.iloc[j,1])):
            total_practice+=hall6_data.iloc[j,1]
            total_mic+=hall6_data.iloc[j,4]
    for j in range(hall6_total):
        if(pd.isna(hall6_data.iloc[j,1])):
            hall6_data.loc[j+hall2_total+hall3_total+hall5_total,"Practice_hours"] = total_practice/(hall6_total-hall6_empty+i)
            hall6_data.loc[j+hall2_total+hall3_total+hall5_total,"Classes_missed"] = total_mic/(hall6_total-hall6_empty+i)
            break
    total_practice=0
    total_mic = 0
#mean for hall12
for i in range(hall12_empty):
    for j in range(hall12_total):
        if(not pd.isna(hall12_data.iloc[j,1])):
            total_practice+=hall12_data.iloc[j,1]
            total_mic+=hall12_data.iloc[j,4]
    for j in range(hall12_total):
        if(pd.isna(hall12_data.iloc[j,1])):
            hall12_data.at[j+hall2_total+hall3_total+hall5_total+hall6_total,"Practice_hours"] = total_practice/(hall12_total-hall12_empty+i)
            hall12_data.at[j+hall2_total+hall3_total+hall5_total+hall6_total,"Classes_missed"] = total_mic/(hall12_total-hall12_empty+i)
            break
    total_practice=0
    total_mic = 0
#median for hall2
for i in range(hall2_empty):
    median_post = []
    median_bh = []
    for j in range(hall2_total):
        if(not pd.isna(hall2_data.iloc[j,2])):
            median_post.append(hall2_data.iloc[j,2])
            median_bh.append(hall2_data.iloc[j,3])
    median_post.sort()
    median_bh.sort()
    n = len(median_post)
    temp_post = 0
    temp_bh = 0
    if(n%2==0):
        temp_post = (median_post[n//2]+median_post[(n//2)+1])//2
        temp_bh = (median_bh[n//2]+median_bh[(n//2)+1])/2
    else:
        temp_post = median_post[n//2]
        temp_bh = median_bh[n//2]
    for j in range(hall2_total):
        if(pd.isna(hall2_data.iloc[j,2])):
            hall2_data.loc[j,"Posts_shared"] = temp_post
            hall2_data.loc[j,"Bulla_hours"] = temp_bh
            break
#median for hall3
for i in range(hall3_empty):
    median_post = []
    median_bh = []
    for j in range(hall3_total):
        if(not pd.isna(hall3_data.iloc[j,2])):
            median_post.append(hall3_data.iloc[j,2])
            median_bh.append(hall3_data.iloc[j,3])
    median_post.sort()
    median_bh.sort()
    n = len(median_post)
    temp_post = 0
    temp_bh = 0
    if(n%2==0):
        temp_post = (median_post[n//2]+median_post[(n//2)+1])//2
        temp_bh = (median_bh[n//2]+median_bh[(n//2)+1])/2
    else:
        temp_post = median_post[n//2]
        temp_bh = median_bh[n//2]
    for j in range(hall3_total):
        if(pd.isna(hall3_data.iloc[j,2])):
            hall3_data.loc[j+hall2_total,"Posts_shared"] = temp_post
            hall3_data.loc[j+hall2_total,"Bulla_hours"] = temp_bh
            break
#median for hall5
for i in range(hall5_empty):
    median_post = []
    median_bh = []
    for j in range(hall5_total):
        if(not pd.isna(hall5_data.iloc[j,2])):
            median_post.append(hall5_data.iloc[j,2])
            median_bh.append(hall5_data.iloc[j,3])
    median_post.sort()
    median_bh.sort()
    n = len(median_post)
    temp_post = 0
    temp_bh = 0
    if(n%2==0):
        temp_post = (median_post[n//2]+median_post[(n//2)+1])//2
        temp_bh = (median_bh[n//2]+median_bh[(n//2)+1])/2
    else:
        temp_post = median_post[n//2]
        temp_bh = median_bh[n//2]
    for j in range(hall5_total):
        if(pd.isna(hall5_data.iloc[j,2])):
            hall5_data.loc[j+hall2_total+hall3_total,"Posts_shared"] = temp_post
            hall5_data.loc[j+hall2_total+hall3_total,"Bulla_hours"] = temp_bh
            break
#median for hall6
for i in range(hall6_empty):
    median_post = []
    median_bh = []
    for j in range(hall6_total):
        if(not pd.isna(hall6_data.iloc[j,2])):
            median_post.append(hall6_data.iloc[j,2])
            median_bh.append(hall6_data.iloc[j,3])
    median_post.sort()
    median_bh.sort()
    n = len(median_post)
    temp_post = 0
    temp_bh = 0
    if(n%2==0):
        temp_post = (median_post[n//2]+median_post[(n//2)+1])//2
        temp_bh = (median_bh[n//2]+median_bh[(n//2)+1])/2
    else:
        temp_post = median_post[n//2]
        temp_bh = median_bh[n//2]
    for j in range(hall6_total):
        if(pd.isna(hall6_data.iloc[j,2])):
            hall6_data.loc[j+hall2_total+hall3_total+hall5_total,"Posts_shared"] = temp_post
            hall6_data.loc[j+hall2_total+hall3_total+hall5_total,"Bulla_hours"] = temp_bh
            break
#median for hall12
for i in range(hall12_empty):
    median_post = []
    median_bh = []
    for j in range(hall12_total):
        if(not pd.isna(hall12_data.iloc[j,2])):
            median_post.append(hall12_data.iloc[j,2])
            median_bh.append(hall12_data.iloc[j,3])
    median_post.sort()
    median_bh.sort()
    n = len(median_post)
    temp_post = 0
    temp_bh = 0
    if(n%2==0):
        temp_post = (median_post[n//2]+median_post[(n//2)+1])//2
        temp_bh = (median_bh[n//2]+median_bh[(n//2)+1])/2
    else:
        temp_post = median_post[n//2]
        temp_bh = median_bh[n//2]
    for j in range(hall12_total):
        if(pd.isna(hall12_data.iloc[j,2])):
            hall12_data.loc[j+hall2_total+hall3_total+hall5_total+hall6_total,"Posts_shared"] = temp_post
            hall12_data.loc[j+hall2_total+hall3_total+hall5_total+hall6_total,"Bulla_hours"] = temp_bh
            break
#setting up relationships
for i in range(hall2_total):
    if(pd.isna(hall2_data.iloc[i,5])):
        hall2_data.loc[i,"Relationship_status"] = "Single_and_stud"
for i in range(hall3_total):
    if(pd.isna(hall3_data.iloc[i,5])):
        hall3_data.loc[i+hall2_total,"Relationship_status"] = "Single_and_stud"
for i in range(hall5_total):
    if(pd.isna(hall5_data.iloc[i,5])):
        hall5_data.loc[i+hall2_total+hall3_total,"Relationship_status"] = "Committed_inside_campus"
for i in range(hall6_total):
    if(pd.isna(hall6_data.iloc[i,5])):
        hall6_data.loc[i+hall2_total+hall3_total+hall5_total,"Relationship_status"] = "Single_and_stud"
for i in range(hall12_total):
    if(pd.isna(hall12_data.iloc[i,5])):
        hall12_data.loc[i+hall2_total+hall3_total+hall5_total+hall6_total,"Relationship_status"] = "Single_and_stud"
#ENTRIES DONE
enthu2 = 0
for i in range(hall2_total):
    e = 0
    if(hall2_data.iloc[i,5]=="Committed_inside_campus"): e = -0.2
    elif(hall2_data.iloc[i,5]=="Single_and_stud"): e = 0.2
    enthu = (hall2_data.iloc[i,1]/18)*0.4+(hall2_data.iloc[i,2]/10)*0.2+(hall2_data.iloc[i,3]/10)*0.2+(hall2_data.iloc[i,4]/8)*(-0.2)+e
    enthu2+=enthu
    hall2_data.loc[i,"Enthu"] = enthu
enthu3 = 0
for i in range(hall3_total):
    e = 0
    if(hall3_data.iloc[i,5]=="Committed_inside_campus"): e = -0.2
    elif(hall3_data.iloc[i,5]=="Single_and_stud"): e = 0.2
    enthu = (hall3_data.iloc[i,1]/18)*0.4+(hall3_data.iloc[i,2]/10)*0.2+(hall3_data.iloc[i,3]/10)*0.2+(hall3_data.iloc[i,4]/8)*(-0.2)+e
    enthu3+=enthu
    hall3_data.loc[i+hall2_total,"Enthu"] = enthu
enthu5 = 0
for i in range(hall5_total):
    e = 0
    if(hall5_data.iloc[i,5]=="Committed_inside_campus"): e = -0.2
    elif(hall5_data.iloc[i,5]=="Single_and_stud"): e = 0.2
    enthu = (hall5_data.iloc[i,1]/18)*0.4+(hall5_data.iloc[i,2]/10)*0.2+(hall5_data.iloc[i,3]/10)*0.2+(hall5_data.iloc[i,4]/8)*(-0.2)+e
    enthu5+=enthu
    hall5_data.loc[i+hall2_total+hall3_total,"Enthu"] = enthu
enthu6 = 0
for i in range(hall6_total):
    e = 0
    if(hall6_data.iloc[i,5]=="Committed_inside_campus"): e = -0.2
    elif(hall6_data.iloc[i,5]=="Single_and_stud"): e = 0.2
    enthu = (hall6_data.iloc[i,1]/18)*0.4+(hall6_data.iloc[i,2]/10)*0.2+(hall6_data.iloc[i,3]/10)*0.2+(hall6_data.iloc[i,4]/8)*(-0.2)+e
    enthu6+=enthu
    hall6_data.loc[i+hall2_total+hall3_total+hall5_total,"Enthu"] = enthu
enthu12 = 0
for i in range(hall12_total):
    e = 0
    if(hall12_data.iloc[i,5]=="Committed_inside_campus"): e = -0.2
    elif(hall12_data.iloc[i,5]=="Single_and_stud"): e = 0.2
    enthu = (hall12_data.iloc[i,1]/18)*0.4+(hall12_data.iloc[i,2]/10)*0.2+(hall12_data.iloc[i,3]/10)*0.2+(hall12_data.iloc[i,4]/8)*(-0.2)+e
    enthu12+=enthu
    hall12_data.loc[i+hall2_total+hall3_total+hall5_total+hall6_total,"Enthu"] = enthu
enthu2 = enthu2/hall2_total
enthu3 = enthu3/hall3_total
enthu5 = enthu5/hall5_total
enthu6 = enthu6/hall6_total
enthu12 = enthu12/hall12_total
if(enthu2>=enthu3 and enthu2>=enthu5 and enthu2>=enthu6 and enthu2>=enthu12): print("Hall 2")
elif(enthu3>=enthu2 and enthu3>=enthu5 and enthu3>=enthu6 and enthu3>=enthu12): print("Hall 3")
elif(enthu5>=enthu3 and enthu5>=enthu2 and enthu5>=enthu6 and enthu5>=enthu12): print("Hall 5")
elif(enthu6>=enthu3 and enthu6>=enthu5 and enthu6>=enthu2 and enthu6>=enthu12): print("Hall 6")
elif(enthu12>=enthu3 and enthu12>=enthu5 and enthu12>=enthu6 and enthu12>=enthu2): print("Hall 12")
hall3_data=hall3_data.reset_index(drop=True)
hall5_data=hall5_data.reset_index(drop=True)
hall6_data=hall6_data.reset_index(drop=True)
hall12_data=hall12_data.reset_index(drop=True)
data = pd.concat([hall2_data, hall3_data], axis=0)
data = pd.concat([data, hall5_data], axis=0)
data = pd.concat([data, hall6_data], axis=0)
data = pd.concat([data, hall12_data], axis=0)
with open('Solved.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Hall", "Practice_hours", "Posts_shared", "Bulla_hours", "Classes_missed", "Relationship_status", "Enthu"])
    for i in range(hall2_total+hall3_total+hall5_total+hall6_total+hall12_total):
        writer.writerow([data.iloc[i,0],data.iloc[i,1],data.iloc[i,2],data.iloc[i,3],data.iloc[i,4],data.iloc[i,5],data.iloc[i,6]])