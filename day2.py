" Day 2
Three Number Sum
Write a function that takes in a non empty array of distinct integers and an integer representing a target sum. 
The function should find a list of triplets in the array that sum upto the target sum and return a two-dimensional array of all the these triplets.
The numbers in each triplet should be order in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.

Sample Input:

array = [12, 2,1, 3, -6, 5, -8, 6]
targetSum = 0

Sample Output:

[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

"

def threeNumberSum(array, targetSum):

  res = []
  for i, x in enumerate(array):
    values = dict()
    for j in range(i+1,len(array)):
      comp = targetSum - array[j] - x
      if comp in values:
        a = min(x, array[values[comp]], array[j])
        b = max (x, array[values[comp]], array[j])
        c = list(set([x, array[values[comp]], array[j]]) -set([a,b]))[0]
        res.append([a,c,b])
        
        # res.append([x, array[values[comp]], array[j]])
        # does'nt work for test case 1
      values[array[j]] = j
  
      
  return sorted(res)
  
  
if __name__ == '__main__':
  
  # array =  [12, 3, 1, 2, -6, 5, -8, 6]
  # targetSum = 0
  
  array = list(map(int, input().split(",")))
  targetSum = int(input())
  print(threeNumberSum(array, targetSum))
  
  