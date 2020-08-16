" Day 25
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: True

Example 2:
Input: s = "rat", t = "car"
Output: False
"

def check_anagram(sentence_1,sentence_2):
  
  sentence_1 = sentence_1.lower()
  sentence_2 = sentence_2.lower()
    
  d = {}
  for x in sentence_2:
    if x == " ":
      continue
    if x not in d:
      d[x] = 1
    else:
      d[x] += 1

  for x in sentence_1:
    if x == " ":
      continue
    if x not in d:
      return False
    else:
      d[x] -= 1
      
      
  if set(d.values()) == {0}:
    return True
  else:
    return False
  
if __name__ == "__main__":
  sentence_1 = "Astronomer"
  sentence_2 = "Moon starer"
  print(check_anagram(sentence_1,sentence_2))



