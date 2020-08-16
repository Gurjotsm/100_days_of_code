" Day 28
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"



def count_island(input_matrix):
  def visit_island(input_matrix, i, j):
    if i >= 0 and i < len(input_matrix) and j >= 0 and j < len(input_matrix[0]) and input_matrix[i][j] == "1":
      input_matrix[i][j] = "0"
      visit_island(input_matrix, i-1, j)
      visit_island(input_matrix, i+1, j)
      visit_island(input_matrix, i, j-1)
      visit_island(input_matrix, i, j+1)
    
  count = 0
  for i in range(len(input_matrix)):
    for j in range(len(input_matrix[0])):
      if input_matrix[i][j] == "1":
        visit_island(input_matrix, i, j)
        count += 1

  return count  
if __name__ == "__main__":
  input_matrix = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
  ]
  print(count_island(input_matrix))




