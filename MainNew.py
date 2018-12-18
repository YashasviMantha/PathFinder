import numpy as np
import random


#Creation of array With all zeros
MainArray = np.zeros(([4,4])) 

# Initianilation of array with numbers
MAT = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
FINISH = MAT[15]
print(FINISH)
START = MAT[0]

for i in range(len(MainArray)):
    for j in range(len(MainArray[i])):
        if(i==3 and j==0):
            MainArray[i][j] = 1
            MAT.remove(1)
        elif(i==0 and j==3):
            MainArray[i][j] = 16
            MAT.remove(16)
        else:
            temp  = random.choice(MAT)
            MAT.remove(temp)
            MainArray[i][j] = temp


# k = 1
# for j in range(len(MainArray)):
#     for i in range(len(MainArray[j])):
#         MainArray[i][j] = k
#         MainArray[i][j] = int(MainArray[i][j])
#         k = k + 1

# Debugging
print(MainArray)

# Bubble Sort Function
def BubbleSort(InArray):
        for i in range(len(InArray)-1):
                for j in range(len(InArray)-i-1):
                        if(InArray[j]<InArray[j+1]):
                                Temp = InArray[j]
                                InArray[j] = InArray[j+1]
                                InArray[j+1] = Temp
        return InArray

# Function that returns all the neighbouring values
def Neighbour(MainArray,POS):
        AllNeiArray = []
        i = POS[0]
        j = POS[1]
        NeighbourDict = {}
        # AllNeiArray.append(MainArray[i][j])             # i,j
        # NeighbourDict[MainArray[i][j]] = [i,j] 
        if(i-1<4 and i-1>=0 and j-1<4 and j-1>=0):
            AllNeiArray.append(MainArray[i-1][j-1])         # i-1,j-1
            NeighbourDict[MainArray[i-1][j-1]] = [i-1,j-1]
        # print("[",i-1,j,"]")
        if(i-1<4 and i-1>=0 and j<4 and j>=0):
            AllNeiArray.append(MainArray[i-1][j])           # i-1,j
            NeighbourDict[MainArray[i-1][j]] = [i-1,j]
            # print("Triggered!")

        if(i-1<4 and i-1>=0 and j+1<4 and j+1>=0):
            AllNeiArray.append(MainArray[i-1][j+1])         # i-1,j+1
            NeighbourDict[MainArray[i-1][j+1]] = [i-1,j+1]

        if(i<4 and i>=0 and j-1<4 and j-1>=0):
            AllNeiArray.append(MainArray[i][j-1])           # i,j-1
            NeighbourDict[MainArray[i][j-1]] = [i,j-1]

        if(i<4 and i>=0 and j+1<4 and j+1>=0):
            AllNeiArray.append(MainArray[i][j+1])           # i,j+1
            NeighbourDict[MainArray[i][j+1]] = [i,j+1]
            # print("Triggered!")


        if(i+1<4 and i+1>=0 and j-1<4 and j-1>=0):
            AllNeiArray.append(MainArray[i+1][j-1])         # i+1,j-1
            NeighbourDict[MainArray[i+1][j-1]] = [i+1,j-1]

        if(i+1<4 and i+1>=0 and j<4 and j>=0):
            AllNeiArray.append(MainArray[i+1][j])           # i+1,j
            NeighbourDict[MainArray[i+1][j]] = [i+1,j]
            # print("Triggered!")


        if(i+1<4 and i+1>=0 and j+1<4 and j+1>=0):
            AllNeiArray.append(MainArray[i+1][j+1])         # i+1,j+1
            NeighbourDict[MainArray[i+1][j+1]] = [i+1,j+1]
            # print("Triggered!")

        # print("AllNeiArray: ",AllNeiArray)
        AllNeiArraySorted = BubbleSort(AllNeiArray)
        # print("Dict: ",NeighbourDict)
        # print("Sorted Array: ",AllNeiArraySorted)
        return  AllNeiArraySorted,NeighbourDict

Flag = 0
Steps = [0]
Inner = 0
CurrentPos = [3,0]
Player = MainArray[3][0]
FINISH = MainArray[0][3]
# while(CurrentPos!=[0,3]):
print("\nSTART",end='-->')
while(Player != FINISH):
    # print()
    # print()

    SortedPos,Dict = Neighbour(MainArray,CurrentPos)
    Player = MainArray[CurrentPos[0]][CurrentPos[1]]
    # Steps.append(Player)
    NewPos = Dict[SortedPos[0]]
    # print("out::::")
    # print("Steps:",Steps)
    # print("SortedArray:",SortedPos)
    print(Player,end="-->")

    for i in range(len(SortedPos)):
        Inner = 0
        for j in range(len(Steps)):
            if(Steps[j] == SortedPos[i]):
                # NewPos = Dict[SortedPos[i]]
                # Steps.append(Player)
                # print("Steps:",Steps)
                # print("SortedArray:",SortedPos)
                Inner = 1
                # break
            

        if(Inner == 1):
            continue
            Inner = 0
        else:
            NewPos = Dict[SortedPos[i]]
            Steps.append(Player)
            break
    CurrentPos = NewPos
    Flag = Flag + 1



    # if(Flag==8):
        # break
        # print("TimeOUT!!!!")




    # print("Element: ",MainArray[NewPos[0]][NewPos[1]],end='   ')
    # print("NewPos: ",NewPos)
    # print("Player: ",Player)
    # print()
    # print() 
        
print("FINISH")
# print(Steps)