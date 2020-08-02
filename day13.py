" Day 13
Function to check if a singly linked list is a palindrome
Given a singly linked list of characters, write a function that returns True if the given list is a palindrome, else False.

Sample input
("r" -> "a" -> "d" -> "a" -> "r" )

Sample output
True
"

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def checkPalindrome(self, l1: ListNode):
      a = ""
      while l1:
        a += str(l1.val)
        l1 = l1.next
  
      rev = ""
      i = len(a) - 1
      while i >= 0:
        rev += a[i]
        i -= 1
        
      if rev == a:
        return True
      else:
        return False
    

l = ListNode("1")
l.next = ListNode("2"); l.next.next = ListNode("3")
l.next.next.next = ListNode("2"); l.next.next.next.next = ListNode("1")
c = Solution()

print(c.checkPalindrome(l))
    
    
    
