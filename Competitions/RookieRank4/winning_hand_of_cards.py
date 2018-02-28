'''
You're at a party and the host has arranged a game of cards. You are given a number of cards and try to create as many combinations from those cards as possible that result in a winning hand. A winning hand is the one where the product of the numbers on the cards modulo a given value, the modulo divisor is equal to another given value, the target value.

Complete the function winningHands to return an integer denoting the number of winning hands.

Input Format

Input contains two lines. The first line contains three space-separated integers  ,  and  denoting the number of cards, the modulo divisor and the target value respectively. The second line contains  space-separated integers. The ith integer denotes the number written on card .

Constraints

Output Format

Print the number of winning hands from the given cards.

Sample Input 0

3 3 2
2 2 2
Sample Output 0

4
Explanation 0

image

Consider the following hands (given by their indices): .

Four hands have product modulo  = .

'''

#!/bin/python3

import sys,itertools

def winningHands(m, x, a):
    # Complete this function
    count = 0
    if m == 1:
        count += sum([len(list(itertools.combinations(a,i))) for i in range(1,len(a)+1)])
        count = 0
        return count
    elif len(set(a)) == 1 and a[0] % m == x:
        count += len(a)
    else:
        count += sum([(1 if t %m == x else 0) for t in a])
    for i in range(2,len(a)+1):
        for j in itertools.combinations(a,i):
            if len(set(j)) == 1:
                count += 1 if pow(j[0],len(j)) % m == x else 0
                continue
            p = 1
            for k in j:
                p *= k
            count += 1 if p % m == x else 0 
    return count

if __name__ == "__main__":
    n, m, x = input().strip().split(' ')
    n, m, x = [int(n), int(m), int(x)]
    a = list(map(int, input().strip().split(' ')))
    result = winningHands(m, x, a)
    print(result)