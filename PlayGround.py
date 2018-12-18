# A = [1,2,3,4,5]
# B = [5,6,1,8,9,10]

flag = 0
# for i in A:
#     flag = 0
#     for j in B:
#         if(i == j):
#             flag = 1
#     if(flag == 0):
#         print("DIE!")
    
#     else:
#         print(i," okay")


MAT = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

import random
import numpy as np

MainArray = np.zeros(([4,4])) 
RAND = [0]

# print(temp)

for i in range(len(MainArray)):
    for j in range(len(MainArray[i])):
        temp  = random.choice(MAT)
        MAT.remove(temp)
        MainArray[i][j] = temp

print(MainArray)
