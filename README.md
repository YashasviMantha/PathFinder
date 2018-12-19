# PathFinder
## My implementation of PathFinder in Python. 

Hai and Welcome!

### The Algorithm:

This is a algorithm that I thought on my own. But, I am not sure if it is already implemented.

**How does this work:**
Lets consider a [4x4] Array. All the elements are initialised to zeros.
Now, we select the start and finish position. By default and at present the Start is [0,3] i.e. Lower Left Corner.
The Finish Position by default and at present is [3,0] i.e. The upper rigt corner.

Now I randomly(Pesudo) asign Numbers in the array. Since, this is a [4x4] array, the total number of elements are 16(1,16 is taken here).
The start position is taken to be 1(The least number) and the finish position is taken to be 16(The highest number).

Now, I made a function which returns a Dictionary and a List:
 - The list has Sorted elements of all the elements neighbouring elements.
 - The Dictonary has the position of the neighbouring elements.
 
 Now, I move the player to the HIGEST Neighbouring element from the initial position.
 
 Hence, after N itrations the player will move to the highest element possible a.k.a the FINISH point!


***NOTE: THIS DOES NOT FIND THE SHORTEST PATH BETWEEN TWO POINTS.***
***This is NOT efficient and very poorly made(I am using BubbleSort).***


WorkInProgress: Will add Garphic Interface.
