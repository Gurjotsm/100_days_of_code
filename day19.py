" Day 19
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
Sample Input -> Output
rotate2('Hello') → 'lloHe'
rotate2('java') → 'vaja'

"

def rotate_left2(s):
  for i in range(2, len(s)):
    print(s[i], end = "")
      
  print(s[0], end = "")
  print(s[1])
  
# rotate_left2("Gurjot")

user_string = input()
rotate_left2(user_string)