from node import *
class StackUsingLinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else :
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        popped = self.head.data
        self.head = self.head.next
        return popped

s = StackUsingLinkedList()
total_elements = int(input('Enter total elements : '))
for i in range(total_elements):
    element = input('Add element : ')
    s.push(element)
p = s.pop()
print(p)
p = s.pop()
print(p)
