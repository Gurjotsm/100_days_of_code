" Day 3
Smallest Difference   
Write a function that takes in two non-empty arrays of integers, find the pair of numbers (one from each array) whose absolute difference is closet to zero, and returns an array containing these two numbers, with the numbsers, with the number from the first array in the first position.

You can assume that there will only be one pair of numbers with the smallest difference.

Sample Input

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample Output

[28, 26]

Optimal Solution
O(nlog(n)) + O(mlog(m) + O(m+n))
where,
n is the size of arrayOne
m is the size of arrayTwo
"

import numpy as np
def smallestDifference(arrayOne, arrayTwo):
 
  min = np.inf
  arrayOne.sort()
  arrayTwo.sort()
  a = 0
  b = 0 
  
  while a < len(arrayOne) and b < len(arrayTwo):
    
    if min > abs(arrayOne[a] - arrayTwo[b]):
      min = abs(arrayOne[a] - arrayTwo[b])
      x, y = arrayOne[a] , arrayTwo[b]
    if arrayOne[a] < arrayTwo[b]:
      a += 1
    else:
      b += 1
      
  return [x, y]
  
if __name__ == "__main__":
  # arrayOne = [-1, 5, 10, 20, 28, 3]
  # arrayTwo = [26, 134, 135, 15, 17]
  
  arrayOne = list(map(int, input().split(",")))
  arrayTwo = list(map(int, input().split(",")))
  print(smallestDifference(arrayOne, arrayTwo))