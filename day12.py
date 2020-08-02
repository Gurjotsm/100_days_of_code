" Day 12
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Sample input
(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)

Sample output
7 -> 8 -> 0 -> 7
"
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      list1 = []
      while l1:
        list1.append(l1.val)
        l1 = l1.next
      list2 = []
      while l2:
        list2.append(l2.val)
        l2 = l2.next
        
        
      i, j = len(list1)- 1, len(list2) -1
      list3 = []
      carry = 0
      while i >= 0 and j >= 0:
        sum = list1[i] + list2[j] + carry
        carry = sum // 10
        digit = sum % 10
        list3.append(digit)
        i -= 1
        j -= 1
        
      while i >= 0:
        sum = list1[i] + carry
        carry = sum // 10
        digit = sum % 10
        list3.append(digit)
        i -= 1
        
      while j >= 0:
        sum = list2[j] + carry
        carry = sum // 10
        digit = sum % 10
        list3.append(digit)
        j -= 1
        
      k = len(list3) - 2
      l3 = ListNode(list3[-1])
      top = l3
      while k >= 0:
        node = ListNode(list3[k])
        top.next = node
        top = top.next
        k -= 1
      print(list3)
      return l3


l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4); l1.next.next.next = ListNode(3)

l2 = ListNode(5); l2.next = ListNode(6); l2.next.next = ListNode(4)
c = Solution()
print(c.addTwoNumbers(l1,l2))
    
    
    
    
