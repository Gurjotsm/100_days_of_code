" Day 14
Given a linked list, remove the n-th node from the end of the list and return its head.
Example:
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
"

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
	length = 0
        start = head
      
        while head:
        	length += 1
        	print(head.val)
          	head = head.next
	n = length + 1 - n
      	i = 1
      	head = start
      	temp = start
      	while i <= n:
        	if i == n:
          		if n == length:
            			temp.next = None
            			break
          		elif n == 1:
            			start = head.next
          		else:
            			temp.next = head.next
        
        	temp = head
        	head = head.next
        	i += 1
      
      return start
  

n = 5    
l1 = ListNode("r")
l1.next = ListNode("c")
l1.next.next = ListNode("e")
l1.next.next.next = ListNode("s")
l1.next.next.next.next = ListNode("d")
n = 5
c = Solution()
print(c.removeNthFromEnd(l1, n))