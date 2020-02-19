class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None



class Tree:
    def insert(self,root,data):
        if root == None:
            return Node(data)
        else:
            if data < root.value:
                cur = self.insert(root.left,data)
                root.left = cur
            else:
                cur = self.insert(root.right,data)
                root.right = cur
        return root
    
    def getHeight(self,root):
        if not root:
            return -1
        if not root.left and not root.right:
            return 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        return max(left_height,right_height) + 1

t = Tree()
root = None
user = int(input('Enter : '))
for i in range(user):
    data = int(input('Enter element : '))
    root=t.insert(root,data)
height = t.getHeight(root)
print(height)