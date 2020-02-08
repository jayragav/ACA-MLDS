import csv
import numpy as np
from random import randint
H5_STRENGTH = 150
H2_STRENGTH = 130
H3_STRENGTH = 140
H12_STRENGTH = 120
H6_STRENGTH = 80

print("Starting dataset generation for practice hours")
hall2_ph = []
for i in range(H2_STRENGTH):
    hall2_ph.append(randint(0,13))

print("Starting dataset generation for posts shared")
hall2_ps = []
for i in range(H2_STRENGTH):
    hall2_ps.append(randint(0,4))

print("Starting dataset generation for bulla hours")
hall2_bh = []
for i in range(H2_STRENGTH):
    hall2_bh.append(randint(0,6))

print("Starting dataset generation for classes missed")
hall2_cm = []
for i in range(H2_STRENGTH):
    hall2_cm.append(randint(0,4))

print("Starting dataset generation for relationship status")
hall2_rs = []
rs = ["Single_and_stud", "Committed_inside_campus", "Long_distance_lover"]
for i in range(H2_STRENGTH):
    hall2_rs.append(rs[randint(0,2)])

print("Starting dataset generation for practice hours")
hall3_ph = []
for i in range(H3_STRENGTH):
    hall3_ph.append(randint(0,15))

print("Starting dataset generation for posts shared")
hall3_ps = []
for i in range(H3_STRENGTH):
    hall3_ps.append(randint(0,5))

print("Starting dataset generation for bulla hours")
hall3_bh = []
for i in range(H3_STRENGTH):
    hall3_bh.append(randint(0,8))

print("Starting dataset generation for classes missed")
hall3_cm = []
for i in range(H3_STRENGTH):
    hall3_cm.append(randint(0,6))

print("Starting dataset generation for relationship status")
hall3_rs = []
rs = ["Single_and_stud", "Committed_inside_campus", "Long_distance_lover"]
for i in range(H3_STRENGTH):
    hall3_rs.append(rs[randint(0,2)])

print("Starting dataset generation for practice hours")
hall5_ph = []
for i in range(H5_STRENGTH):
    hall5_ph.append(randint(0,14))

print("Starting dataset generation for posts shared")
hall5_ps = []
for i in range(H5_STRENGTH):
    hall5_ps.append(randint(0,5))

print("Starting dataset generation for bulla hours")
hall5_bh = []
for i in range(H5_STRENGTH):
    hall5_bh.append(randint(0,6))

print("Starting dataset generation for classes missed")
hall5_cm = []
for i in range(H5_STRENGTH):
    hall5_cm.append(randint(0,4))

print("Starting dataset generation for relationship status")
hall5_rs = []
rs = ["Single_and_stud", "Committed_inside_campus", "Long_distance_lover"]
for i in range(H5_STRENGTH):
    hall5_rs.append(rs[randint(0,2)])
print("Starting dataset generation for practice hours")
hall6_ph = []
for i in range(H6_STRENGTH):
    hall6_ph.append(randint(0,20))

print("Starting dataset generation for posts shared")
hall6_ps = []
for i in range(H6_STRENGTH):
    hall6_ps.append(randint(0,7))

print("Starting dataset generation for bulla hours")
hall6_bh = []
for i in range(H6_STRENGTH):
    hall6_bh.append(randint(0,4))

print("Starting dataset generation for classes missed")
hall6_cm = []
for i in range(H6_STRENGTH):
    hall6_cm.append(randint(0,2))

print("Starting dataset generation for relationship status")
hall6_rs = []
rs = ["Single_and_stud", "Committed_inside_campus", "Long_distance_lover"]
for i in range(H6_STRENGTH):
    hall6_rs.append(rs[randint(0,2)])
print("Starting dataset generation for practice hours")
hall12_ph = []
for i in range(H12_STRENGTH):
    hall12_ph.append(randint(0,16))

print("Starting dataset generation for posts shared")
hall12_ps = []
for i in range(H12_STRENGTH):
    hall12_ps.append(randint(0,7))

print("Starting dataset generation for bulla hours")
hall12_bh = []
for i in range(H12_STRENGTH):
    hall12_bh.append(randint(0,12))

print("Starting dataset generation for classes missed")
hall12_cm = []
for i in range(H12_STRENGTH):
    hall12_cm.append(randint(0,5))

print("Starting dataset generation for relationship status")
hall12_rs = []
rs = ["Single_and_stud", "Committed_inside_campus", "Long_distance_lover"]
for i in range(H12_STRENGTH):
    hall12_rs.append(rs[randint(0,2)])


print("Starting csv generation, with seeded random missing indices")
with open('galaxy_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Hall", "Practice_hours", "Posts_shared", "Bulla_hours", "Classes_missed", "Relationship_status", "Enthu"])
    rand_miss_indices = []
    for i in range(20):
        rand_miss_indices.append(randint(0, H2_STRENGTH))

    for i in range(H2_STRENGTH):
        if i not in rand_miss_indices:
            writer.writerow(["2", hall2_ph[i], hall2_ps[i], hall2_bh[i], hall2_cm[i], hall2_rs[i], 0])
        else:
            writer.writerow(["2", None, None, None, None, None, 0])
    
    for i in range(30):
        rand_miss_indices.append(randint(0, H3_STRENGTH))
    for i in range(H3_STRENGTH):
        if i not in rand_miss_indices:
            writer.writerow(["3", hall3_ph[i], hall3_ps[i], hall3_bh[i], hall3_cm[i], hall3_rs[i], 0])
        else:
            writer.writerow(["3", None, None, None, None, None, 0])

    for i in range(25):
        rand_miss_indices.append(randint(0, H5_STRENGTH))
    for i in range(H5_STRENGTH):
        if i not in rand_miss_indices:
            writer.writerow(["5", hall5_ph[i], hall5_ps[i], hall5_bh[i], hall5_cm[i], hall5_rs[i], 0])
        else:
            writer.writerow(["5", None, None, None, None, None, 0])

    for i in range(10):
        rand_miss_indices.append(randint(0, H6_STRENGTH))
    for i in range(H6_STRENGTH):
        if i not in rand_miss_indices:
            writer.writerow(["6", hall6_ph[i], hall6_ps[i], hall6_bh[i], hall6_cm[i], hall6_rs[i], 0])
        else:
            writer.writerow(["6", None, None, None, None, None, 0])

    for i in range(15):
        rand_miss_indices.append(randint(0, H12_STRENGTH))
    for i in range(H12_STRENGTH):
        if i not in rand_miss_indices:
            writer.writerow(["12", hall12_ph[i], hall12_ps[i], hall12_bh[i], hall12_cm[i], hall12_rs[i], 0])
        else:
            writer.writerow(["12", None, None, None, None, None, 0])
print("done")
