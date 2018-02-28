'''
DNA sequence chains are made of nucleobases or nucleotides namely , ,  and . Substrings in a DNA sequence are often indicative of amino acid chains, i.e proteins.

Your goal is to find the longest prefix that repeats itself before and after each position, with the prefix overlapping at that position alone. In other words, if you are looking at the sequence item , the substring ending at position :  is the same as the substring beginning at position : . Both of those substrings must match a  length prefix: . Compute the length of the longest substring for which all three conditions hold, i.e for every index , the largest value of  is to be computed such that  =  = .

For example, consider the following arbitrary nucleotide sequence. For each index , the largest possible value of  is shown below it.

image

Note: At  and , two values of  and  both hold good.  is the correct answer since it is the larger value.

Complete the function piVsZ which accepts an input string and returns an integer array denoting the largest value of  for each character of the input string.

Input Format

Input contains single string  consisting of lowercase English letters, .

Constraints

Length of  doesn't exceed 

Output Format

Output  integers for each  between 0 and : maximum integer , such that .

Sample Input 0

babbabababb
Sample Output 0

1 0 1 1 0 3 0 3 0 1 1
Explanation 0

For the string  = babbabababb, for every index , the largest value of  is computed such that  =  = .

For example,

For , at , . Hence the largest vaue of  to satisfy the condition is .
For , no such  is feasible, hence resulting in  and .
For , two values of ,  and , satisfy the given condition. In such a case, , the largest value of should be chosen.
The table below illustrates how  is computed for every character in the string.

Note:  denotes empty/null set.

0		b	b	b
1				
2		b	b	b
3		b	b	b
4				
5		bab	bab	bab
6		b	b	b
7		bab	bab	bab
8				
9		b	b	b
10		b	b	b
'''

#!/bin/python3

import sys

def DNAValue(s):
    # Complete this function
    results = []
    for i in range(len(s)):
        if i == 0: 
            results.append(1)
            continue
        if i == 1: 
            if len(s) >= 3:
                results.append(2 if s[i-1:i+1] == s[i:i+2] else  1 if s[i] == s[i-1] else 0)
            else:
                results.append(1 if s[1] == s[0] else 0)
            continue
        min_possible_size = min(len(s[:i+1]),len(s[i:]))
        max_match = 0
        #if len(set(s)) == 1:
        #    results.append(min_possible_size)
        #    continue
        if s[i] != s[0]:
            results.append(0)
            continue
        for j in range(1,min_possible_size+1):
            s1 = s[i-j+1:i+1]
            s2 = s[i:i+j]
            s3 = s[:j]
            if s1[0] != s1[-1]:
                continue
            if s1 == s2 and s1 == s3:
                max_match = j
       
        results.append(max_match)            
    return results           
        
        

if __name__ == "__main__":
    s = input().strip()
    result = DNAValue(s)
    print (" ".join(map(str, result)))