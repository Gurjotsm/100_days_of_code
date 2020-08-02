" Day 6
Move Element to End

You're given an array of integers and an integer. Write a function that moves all instance of that integer in the array to the end of the array and returns the array.

Write a function that should perform this in place (i.e , it should mutate the input array) and doesn't need too maintain the order of the other integer.

Sample Input;

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

Sample Output:

[1, 3, 4, 2, 2,2,2,2] // the number 1, 3, and 4 could be ordered differently
Time Complexity:

O(n) time | O(1) space,
where n, is the length of the array
"

def moveElementToEnd(array, toMove):

  y = len(array) - 1
  x = 0
  while x < y:
    if array[x] == toMove:
      if array[y] != toMove:
        array[x], array[y] = array[y], array[x]
      else:
        y -= 1
    else:
      x += 1
    
  return array
    
  
        
if __name__ == "__main__":
  # array = [2, 1, 2, 2, 2, 3, 4, 2]
  # toMove = 2
  
  array = list(map(int, input().split(",")))
  toMove = int(input())
  print(moveElementToEnd(array, toMove))