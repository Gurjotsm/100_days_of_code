" Day 7
Monotonic Array
Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non -decreasing.

Sample Input:
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
Sample Output:
True
Time Complexity:  O(n) time | O(1) space, where n, is the length of the array
"

def monoArray(array):
  increasing = True
  decreasing = True
  for x in range(len(array)-1):
    print(array[x])
    if array[x] > array[x+1]:
      increasing = False
    elif array[x] < array[x+1]:
      decreasing = False
  return increasing or decreasing

if __name__ == "__main__":
  array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
  # array = [1,100,1000]
  print(monoArray(array))