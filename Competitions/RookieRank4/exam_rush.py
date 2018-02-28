'''
Your final exam is approaching and you haven't begun to study. In order to have the best chance of passing the course, you resolve to study from now until exam time. Chapters vary in length, but not in value towards a passing grade, so you want to study as many complete chapters as possible. The order of chapters doesn't matter, but you must complete a chapter before it will help your grade.

Your task is to maximize the number of complete chapters you can study between now and exam time.

Complete the function examRush to return the integer value representing the maximum number of chapters you can study before the exam.

Input Format

The first line contains an integer number,  (number of chapters) and an integer number,  (hours left until the exam). Then there are  lines, each containing the time,  in hours required to study that chapter.

Constraints

Output Format

Print an integer number, which is the maximum number of chapters that can be studied completely before the start of the final examination.

Sample Input 0

2 2
1
2
Sample Output 0

1

'''

import sys

def examRush(tm, t):
    # Complete this function
    stm = sorted(tm)
    time = 0
    count = 0
    #print(stm)
    for i in stm:
        if i+time <= t:
            time += i
            count  += 1
    return count

if __name__ == "__main__":
    n, t = input().strip().split(' ')
    n, t = [int(n), int(t)]
    tm = []
    tm_i = 0
    for tm_i in range(n):
       tm_t = int(input().strip())
       tm.append(tm_t)
    result = examRush(tm, t)
    print(result)
