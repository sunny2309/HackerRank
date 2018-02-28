'''
This problem will deal with trees. A few definitions follow:

internal node: any node of a tree with child elements (children)
external node or leaf: any node of a tree without children
root node: topmost node of a tree
node height: distance of a node from its most distant leaf
tree height: synonymous with root height, node height of the root node
A Binary Search Tree (BST), also called ordered binary tree, is a type of binary tree where the nodes are arranged in order. A BST has the following properties:

Each node has a unique value*.
A total order is defined on these values.
The left subtree of a node contains only values less than the node's value.
The right subtree of a node contains only values greater than the node's value.
* No duplicates. Be careful.

You will be given an array of integers to insert into a BST that you create. Complete the heightOfBST function below to return an integer array. The first element should be the tree height of the BST and the second element should be the sum of the heights of all of the BST nodes, the total height.

Input Format

In the first line you will be given an integer  which represents the number of space-separated integers in the following line. In the following line, there are  space-separated integers , denoting the values to be inserted into the BST in this exact order.

Constraints

Output Format

Return an integer array of two elements:  to be printed by the code stub.

Sample Input 0

8
500 400 300 450 425 475 600 550
Sample Output 0

3
7
Explanation 0

The image below shows the completed BST and the height of each of the nodes:



'''


#!/bin/python3

import os
import sys,copy
sys.setrecursionlimit(10000)
class Node(object):
    def __init__(self,weight):
        self.parent = None
        self.weight = weight
        self.height = 0
        self.left = None
        self.right = None
    
# Complete the function below.
heights = []
def traverse(node):
    if node.left:
        traverse(node.left)
    heights.append(node.height)
    #print(node.height)
    if node.right:
        traverse(node.right)

def heightAndTotalHeight(arr):
    # Write your code here.
    #count = 0
    arr2 = []
    for j in arr:
        if j not in arr2:
            arr2.append(j)
    if arr:
        root  = Node(arr2[0])
        for w in arr2[1:]:
            temp = root
            while True:
                p = temp
                left_set = right_set = False
                if w < temp.weight:
                    temp = temp.left
                    left_set = True
                else:
                    temp = temp.right
                    right_set = True
                if not temp:
                    temp = Node(w)
                    temp.parent = p
                    if left_set:
                        p.left = temp
                    if right_set:
                        p.right = temp
                    if not (p.left and p.right):
                        while p:
                            h = max(p.left.height,p.right.height) if p.left and p.right else p.right.height if p.right else p.left.height
                            #print(h)
                            p.height = h + 1
                            p = p.parent
                        #count += 1
                    break

        traverse(root)

    return (root.height,sum(heights)) if arr else (0,0)
                

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    arr_size = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = heightAndTotalHeight(arr)

    f.write("\n".join(map(str, result)))

    f.write('\n')

    f.close()
