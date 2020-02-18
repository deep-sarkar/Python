'''
    -LIFO algorithm
'''
class Stack:
    def __init__(self):
        self.my_satck = []
    
    def push(self,data):
        return self.my_satck.append(data) #Add data at last position
    
    def pop(self):
        return self.my_satck.pop()  #delete data from last position
    
    def peek(self):
        return self.my_satck[len(self.my_satck) - 1]
    
    def is_empty(self):
        return self.my_satck == []
    
    def size(self):
        return len(self.my_satck)