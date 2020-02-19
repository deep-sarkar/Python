class Deque:
    def __init__(self):
        self.item = []
    
    def size(self):
        return len(self.item) - 1
    
    def empty(self):
        return len(self.item) == 0
    
    def addFront(self,data):
        self.item.append(data)

    def addReae(self,data) :
        self.item.insert(0, data)

    def removeFront(self):
        return self.item.pop()
    
    def removeRear(self):
        return self.item.pop(0)
    
    def view(self):
        print(self.item)