" Day 11
Write a Python program to search a specific item in a singly linked list and return true if the item is found otherwise return false.
Sample input
items = singly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')
items.search_item('SQL')

Sample output
False
"

class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
        
class singly_linked_list:
    def __init__(self):
        # Createe an empty list
        self.tail = None
        self.head = None
        self.count = 0
        
    def append_item(self, data):
        #Append items on the list
        new_value = Node(data)
        if self.head == None:
          self.head = new_value
          self.tail = new_value
        else:
          self.tail.next = new_value
          self.tail = self.tail.next
          self.tail.next = None
        
    def search_item(self, val):
        # Search the list
        start = self.head
        while self.head.next != None:
          if self.head.data == val:
            self.head = start
            return True
          else:
            self.head = self.head.next
            
        # just to check for last item in linked list
        if self.head.data == val:
          self.head = start
          return True
        self.head = start
        return False
      
      

if __name__ == "__main__":
  items = singly_linked_list()
  items.append_item('PHP')
  items.append_item('Python')
  items.append_item('C#')
  items.append_item('C++')
  items.append_item('Java')
  
  print(items.search_item('C#'))
  print(items.search_item('Python'))