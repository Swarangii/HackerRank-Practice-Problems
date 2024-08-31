#Problem:

'''Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example : records = [["chi",20.0],["beta",50.0],["alpha",50.0]]
The ordered list of scores is [20.0,50.0], so the second lowest score is 50.0. There are two students with that score:["alpha","beta"] . Ordered alphabetically, the names are printed as:

alpha
beta

Input Format:

The first line contains an integer,N , the number of students.
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints:

2<=N<=5
There will always be one or more students having the second lowest grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

'''
#Solution:
if __name__ == '__main__':
    marksheet=[]
    scoresheet=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet+=[[name,score]]
        scoresheet+=[score]
    x = sorted(set(scoresheet))[1]
    for n , s in sorted(marksheet):
        if s==x:
            print(n)

#Sample Input:
"""
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""

#Sample Output:
"""
Berry
Harry
"""