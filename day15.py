" Day 15
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.
For example, given the following linked lists :
5 -> 8 -> 20 
4 -> 11 -> 15
The merged list should be :
4 -> 5 -> 8 -> 11 -> 15 -> 20
"

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoLinkedLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      
      if l1.val < l2.val:
        start = l1
        l1 = l1.next
      else:
        start = l2
        l2 = l2.next
        
      temp = start
      while l1 and l2:
        if l1.val < l2.val:
          temp.next = l1
          l1 = l1.next
        else:
          temp.next = l2
          l2 = l2.next
        temp = temp.next
          
      while l1:
        temp.next = l1
        l1 = l1.next
        temp = temp.next
      
      while l2:
        temp.next = l2
        l2 = l2.next
        temp = temp.next
    
      ## to print nodes of start  
      # while start:
      #   print(start.val)
      #   start = start.next
        
      return start

    
    
c = Solution()
l1 = ListNode(5); l1.next = ListNode(8); l1.next.next = ListNode(20)
l2 = ListNode(4); l2.next = ListNode(11); l2.next.next = ListNode(15)
print(c.addTwoLinkedLists(l1, l2))
    
    
