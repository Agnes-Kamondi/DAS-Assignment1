class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
 
def insert(root, data):
    if not root:
        return Node(data)
 
    if data < root.data:
        root.left = insert(root.left, data)
    if data > root.data:
        root.right = insert(root.right, data)
     
    return root

def maxValue(root):
    value = root
     
    while(value.right):
        value = value.right
    return value.data
 
if __name__=='__main__':
    root=None
    root = insert(root,20)
    root = insert(root,10)
    root = insert(root,30)
    root = insert(root,60)
    root = insert(root,50)
    print(maxValue(root))
 