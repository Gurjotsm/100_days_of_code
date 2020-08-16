" Day 23
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: True

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: False
"


def binary_search(a, x, low, high):
  
  while low <= high:
    mid = (low + high)// 2
    
    if type(a[mid]) == list:
      val = a[mid][0]
    else:
      val = a[mid]
      
    if val == x:
      return mid
    elif val > x:
      high = mid - 1
    else:
      low = mid + 1
      
      
  return low - 1
  
def find_target(input_matrix,target):
  
  if not input_matrix[len(input_matrix) - 1]:
    return False
  low1, low2 = 0, 0
  high1, high2 = len(input_matrix) - 1, len(input_matrix[0]) - 1
  
  i = binary_search(input_matrix, target, low1, high1)
  j = binary_search(input_matrix[i], target, low2, high2)
  
  
  if input_matrix[i][j] == target:
    return True
  else:
    return False
          
    
if __name__ == "__main__":
  input_matrix = [[]]
  target = 11
  print(find_target(input_matrix,target))




