'''
You are appointed as a system admin in a firm, and it is your responsibility to check the safety of the server racks in one of the server rooms. The server racks are arranged in an array. If any rack reaches another rack when it falls, it will cause the other rack to fall. Safety rules require that at least some of the racks should remain standing if one of the ends falls toward the others.

Your task is to determine whether either or both ends will cause all racks to fall should one be tipped. To determine if a rack will knock over another rack, use the following two rules*:

Left rack falls:  + 
Right rack falls:  - 
* Assume the position of a rack is  and its height is .

The test is based on a single event. In other words, if it takes toppling both the left and right ends to knock down all the servers, you still pass the safety inspection.

An example follows:

In the image shown below, rack  can trigger the fall of rack  since , but rack  can't trigger the fall of rack  since .

image

Complete the function checkAll, which takes the positions and heights of the server racks as input, and return  representing which of the ends is unsafe.

Input Format

In the first line, the number of racks, , will be given. 
In the second line, the position of each rack, , will be given. 
In the third line, the height of each rack, , will be given.

Constraints

Output Format

If the racks fall over no matter from which end it gets triggered, then return BOTH. If the racks fall over due to rack at leftmost or rightmost, then return LEFT or RIGHT respectively. If neither end toppling will cause all the racks to fall over, return NONE.

Sample Input 0

5
1 2 3 4 5
1 1 1 1 1
Sample Output 0

BOTH
Explanation 0

Each of the piles in this case are situated 1 unit away from each other, and the height of each pile is also 1 unit. All of the piles will fall over regardless of the side which is pushed over.

image

Sample Input 1

5
1 2 3 4 8
1 1 1 1 1
Sample Output 1

NONE
Explanation 1

If the leftmost pile is pushed over, only the first four piles will fall over. The last pile will remain untouched, as none of the previous ones can reach it. Similarly, if the rightmost pile is pushed over, it can't reach any of the others.

image

Medium
Submitted 5 times
Max Score 20
Need Help?
View Discussions
View Editorial Solution
View Top Submissions
Rate This Challenge:
    
Download problem statement
Download all test cases
Suggest Edits
Current Buffer (saved locally, editable)     


'''


#!/bin/python3

import sys

def checkAll(n, height, position):
    right = [0]*max(position)
    left =  [0]*max(position)
    for p,h in list(zip(position,height))[:-1]:
        k = p+h
        #print(p,k)
        left[p:k] = [1]*len(left[p:k])
    #print('RIGHT')
    for p,h in list(reversed(list(zip(position,height))))[:-1]:
        k = 0 if p-h-1 < 0 else p-h-1
        #print(k,p-1)
        right[k:p-1] = [1]*len(right[k:p-1])
    #print(right,left)
    return 'BOTH' if 0 not in left[min(position):] and 0 not in right[min(position)-1:-1] else 'LEFT' if 0 not in left[min(position):] else 'RIGHT' if 0 not in right[min(position)-1:-1] else 'NONE'
   
if __name__ == "__main__":
    n = int(input().strip())
    position = list(map(int, input().strip().split(' ')))
    height = list(map(int, input().strip().split(' ')))
    ret = checkAll(n, height, position)
    print(ret)


