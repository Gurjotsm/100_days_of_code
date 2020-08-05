" Day 18
Given 2 sets of integers,  M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  M or N  but do not exist in both.

Input Format
The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output Format
Output the symmetric difference integers in ascending order, one per line.

Sample Input
4
2 4 5 9
4
2 4 11 12
Sample Output
5
9
11
12
"

def symmetric_difference(a, b):
  
  sol = []
  for x in a:
    if x not in b:
      sol.append(x)
      
  for y in b:
    if y not in a:
      sol.append(y)
    
  sol = sorted(sol)
  for x in sol:
    print(x)
  
  
length1 = int(input())
set1 = set(map(int, input().split()))
length2 = int(input())
set2 = set(map(int, input().split()))
symmetric_difference(set1, set2)