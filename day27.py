" Day 27
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.
Example 1:
Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"

Example 2:
Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"
"



# time complexity is O(m*n) where m is length of longest word and n is total words
def return_vertically(input_string):
  input_list = input_string.split()
  length = 0
  for x in input_list:
    if length < len(x):
      length = len(x)
      
  i = 0
  res = [""]*length

  while i != length:
    for x in input_list:
      try:
        res[i] += x[i]
      except IndexError:
        res[i] += " "
    i += 1
    
  # removing trailing spaces
  # for i in range(len(res)):
  #   while res[i][len(res[i]) -1] == " ":
  #     res[i] = res[i][:len(res[i]) -1]
  
  for i in range(len(res)):
    res[i] = res[i].rstrip()
  
  return res
    
if __name__ == "__main__":
  input_string = "TO BE OR NOT TO BE"
  print(return_vertically(input_string))




