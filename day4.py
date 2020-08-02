" Day 4
Four Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all quadruplets in the array that sum up to the largest sum and return a two dimensional array of all these
quadruplets in no particular order.

This is the last of its kind, I hope you would have understood the concept of storing complements in the set / dictionary or after sorting the list we can use two pointers to decide whether to decrement / increment the pointers. This problem also works on the similar principle, so don't get trapped into the 4 loop Naive Solution.

Sample Input

array = [7,6,4,-1,1,2]
targetSum = 16

Sample Output
// the quadruplets could be ordered differently
[[7, 6, 4, -1], [7, 6, 1, 2]]

Optimal Space & Time Complexity

Average: O(n^2) time | O(n^2) space - where n is the length of the input arrayTwo
Worst: O(n^3) time | O(n^2) space - where n is the length of the input array
"

def fourNumberSum(array, targetSum):
  assert len(array) > 0, "Empty array! "
  assert len(array) == len(set(array)), "Duplicate values! "
  
  two_sum_values = dict()
  for i in range(len(array)-1):
    for j in range(i+1, len(array)):
      if array[i] + array[j] in two_sum_values:
        two_sum_values[array[i] + array[j]] = [two_sum_values[array[i] + array[j] ], [i,j] ]
      
      two_sum_values[array[i] + array[j]] = [i, j]
  
  
  res = []
  for i in range(len(array) - 1):
    for j in range(i + 1, len(array)):
      two_sum = array[i] + array[j]
      if targetSum - two_sum in two_sum_values:
        indexes = [two_sum_values[targetSum - two_sum]]
        for ind in indexes:
          a = ind[0]
          b = ind[1]
          if len(set([i,j,a,b])) == 4:
            indices = [array[i],array[j],array[a],array[b]]
            indices.sort()
            if indices not in res:
              res.append(indices)
    
  return res
  
if __name__ == "__main__":
  # array = [7,6,4,-1,1,2]
  # targetSum = 16
  
  array = list(map(int, input().split(",")))
  targetSum = int(input())
  print(fourNumberSum(array, targetSum))
  