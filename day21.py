" Day 21
Instructions from your teacher:
Write a  program to find maximum of each column of  2d array 
Sample Input -> Output
max_col([[1, 5, 13], [11], [9, 18]]) → [11, 18, 13] 
max_col([[1, 8, 1], [1,21], [9]]) → [9, 21, 1]
"

import itertools 

def max_col(test_list):
  
  width = 0
  for x in test_list:
    if len(x) > width:
      width = len(x)
      
  res = [0]*width
  for x in test_list:
    i = 0
    for y in x:
      if y > res[i]:
        res[i] = y
      i += 1
    

  return res  
  
if __name__ == "__main__":
  input_list = [[1, 8, 1], [1,21], [9]]
  print(max_col(input_list))




