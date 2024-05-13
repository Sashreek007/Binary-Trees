from using_linked_list import Queue
class BSTNode:
    def __init__(self,data):
        self.data= data
        self.leftChild=None
        self.rightChild= None


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def insert(rootnode,value):
    if rootnode.data== None:
        rootnode.data=value
    elif value<=rootnode.data:
        if rootnode.leftChild is None:
            rootnode.leftChild=BSTNode(value)
        else:
            insert(rootnode.leftChild,value)
    elif value>rootnode.data:
        if rootnode.rightChild is None:
            rootnode.rightChild=BSTNode(value)
        else:
            insert(rootnode.rightChild,value)
    return "Successful"



#Traversal is same as Binary Trees

def search(rootnode,nodevalue):
    if rootnode is None:
        return "Not Found"
    if rootnode.data == nodevalue:
        return "Found"
    elif rootnode.data>nodevalue:
        if rootnode.leftChild.data==nodevalue:
            return "Found"
        else:
            search(rootnode.leftChild,nodevalue)
    else:
        if rootnode.rightChild.data==nodevalue:
            return "Found"
        else:
            search(rootnode.rightChild,nodevalue)

def minValueNode(rootnode):
    current = rootnode
    while (current.leftChild is not None):
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

def delete(rootnode):
    rootnode.data=None
    rootnode.leftChild=None
    rootnode.rightChild=None

newBST = BSTNode(None)
insert(newBST, 70)
insert(newBST,50)
insert(newBST,90)
insert(newBST,30)
insert(newBST,60)
insert(newBST,80)
insert(newBST,100)
insert(newBST,20)
insert(newBST,40)
levelOrderTraversal(newBST)
deleteNode(newBST,30)
levelOrderTraversal(newBST)
