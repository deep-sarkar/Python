from node import *
class QueueUsingLinkedList:
    def __init__(self):
        self.head = None
    
    def enque(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def dequeue(self):
        if self.head == None:
            print('Queue is empty')
        else:
            temp = self.head
            previous = None
            while temp.next != None:
                previous,temp = temp,temp.next
            data = temp.data
            previous.next = None
            return data
    
    def display(self):
        if self.head == None:
            print('Queue is empty')
        else:
            temp = self.head
            while temp != None:
                print(temp.data,end=" ")
                temp = temp.next
    
    def size(self):
        temp = self.head
        count = 0
        if self.head == None:
            return 0
        while temp.next != None:
            count += 1
            temp = temp.next
        return count
        