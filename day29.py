" Day 29
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:
Will share image in whatsapp group

Note:
The total number of elements of the given matrix will not exceed 10,000.

"

def return_diag(input_matrix):
  res = []
  indexes = {}
  # the diagonal elements have same index
  for i in range(len(input_matrix)):
    for j in range(len(input_matrix[0])):
      indexes.setdefault(i + j, []).append(input_matrix[i][j])
  
  # the order helps us to iterate correctly
  order = False
  for x in indexes.keys():
    if order == True:
      order = False
      res.extend(indexes[x])
    
    elif order == False:
      order = True
      res.extend(indexes[x][::-1])
      
  return res
  
if __name__ == "__main__":
  input_matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
  ]
  print(return_diag(input_matrix))




