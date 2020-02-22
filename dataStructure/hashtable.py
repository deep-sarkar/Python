class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.size = 11
        self.bucket = [None] * self.size

    '''
        - hash(value) takes an integer value as an input and return hash code
    '''
    def hash(self,value):
        hash_code = value%11
        return hash_code

    '''
        -insert(value) takes integer value as an input and add it in a node according to position of
            hash code
    '''
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
    
    '''
        -find(value) takes integer as an input and search it in table according to its hashcode
    '''
    def find(self,value):
        hash_code = self.hash(value)
        node = self.bucket[hash_code]
        while node != None and node.value != value:
            node = node.next
        if node is None:
            return False
        return True    

    '''
        remove(value) method is used to remove any value ffrom hash table
    '''
    def remove(self,value):
        hash_code = self.hash(value)
        node = self.bucket[hash_code]
        prev = None
        while node is None or node.value != value:
            prev = node
            node = node.next
        if node is None:
            return "Value not present"
        else:
            if prev == None:
                return "Value not present"
            else:
                data = node.value
                prev.next = prev.next.next
                return "removed"

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

remove = h.remove(13)
print('Remove :',remove)

find = h.find(13)
print('Find : 13',find)
