" Day 17
Given a singly linked list and an integer K, reverses the nodes of the
list K at a time and returns modified linked list.
NOTE : The length of the list is divisible by K
Example :
Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5
"

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapLinkedLists(self, l1: ListNode,key: int) -> ListNode:

      k = 0
      solution = []
      temp = []
      while l1:
        
        if k != key:
          k += 1
        else:
          solution.extend(temp[:: -1])
          k = 1
          temp = []
          
        temp.append(l1.val)
        l1 = l1.next
      
      # to add last pairs
      solution.extend(temp[:: -1])
      # print(solution)
      
      x = 1
      l1 = ListNode(solution[0])
      temp = l1
      while x < len(solution):
        node = ListNode(solution[x])
        temp.next = node
        temp = temp.next
        x += 1
          
      return l1
          
          
      
# custom test case     
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3); l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)
l2 = l1.next.next.next.next.next
l2.next = ListNode(7)
l2.next.next = ListNode(8)
key = 2
c = Solution()

print(c.swapLinkedLists(l1, key))