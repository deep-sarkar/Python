class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.size = 11
        self.bucket = [None] * self.size

    def hash(self,value):
        hash_code = value%11
        return hash_code
    
    def insert(self,value):
        hash_code = self.hash(value)
        node = self.bucket[hash_code]
        if node is None:
            self.bucket[hash_code] = Node(hash_code,value)
            return
        prev = node
        while node != None:
            prev = node
            node = node.next
        prev.next = Node(hash_code,value)
    
    def find(self,value):
        hash_code = self.hash(value)
        node = self.bucket[hash_code]
        while node != None and node.value != value:
            node = node.next
        if node is None:
            return False
        return True    


h = HashTable()
data = [12,23,54,68,95,4,7,64,13,97,85,21,66,58]
for element in data:
    print(element,end= " ")
    h.insert(element)

print()
find = h.find(13)
print('Find : 13',find)
find = h.find(100)
print('Find : 100',find)
find = h.find(66)
print('Find : 66',find)


