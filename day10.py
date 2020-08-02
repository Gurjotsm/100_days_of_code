" Day 10
Ceasar Cipher Encryptor
Given a non-empty string of lowercase letters and a non-negative integer representing a key, Write a function that returns a new string obtained by shifting any letter in the input string by k positions in the alphabet, where k is the key. Note that letters should "wrap" around the alphabet; in other words, the letter "z" shifted by one returns the letter "a"
Sample Input:
string = "xyz"
key = 2

Sample Output:
"zab"

Optimal Space & Time Complexity
O(1) & O(n), where n is the length of the input string. 
"

def caesarCipherEncryptor(string, key):
  res = ""
  key = key%26
  for x in string:
    val = ord(x) + key
    if val > 122:
      val -= 26
      
    res += chr(val)
  return res
  
  
string = "xyz"
key = 30
print(caesarCipherEncryptor(string, key))