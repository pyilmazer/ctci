import sys
class BinaryNode:
   def __init__(self,id,visited=False,left=None,right=None,parent=None):
       if not id:
           id = -1
       self.id=id
       self.visited=visited
       self.left=left
       self.right=right
       self.parent=parent

   def __str__(self):
       return str(self.id)

def inOrder(nodePtr):
   if nodePtr:
       inOrder(nodePtr.left)
       sys.stdout.write(str(nodePtr.id) + ' ')
       inOrder(nodePtr.right)


def inOrderSuccessor(nodePtr):
    if not nodePtr:
        return None
    if nodePtr.right:
        return getLeftMostNode(nodePtr.right)
    else:
        node=nodePtr
        parent=nodePtr.parent

        while parent and parent.right is node:
            node=parent
            parent=parent.parent
        return parent

def getLeftMostNode(nodePtr):
    node=nodePtr
    while node.left:
        node=node.left
    return node


if __name__ == "__main__":
    print("hebele")
    root=BinaryNode(16)
    root.left=BinaryNode(8,parent=root)

    root.left.left=BinaryNode(5,parent=root.left)
    root.left.right=BinaryNode(11,parent=root.left)
    root.left.left.left=BinaryNode(3,parent=root.left.left)
    root.left.left.right=BinaryNode(6,parent=root.left.left)

    root.left.right.right=BinaryNode(14,parent=root.left.right)

    root.right=BinaryNode(25,parent=root)
    root.right.left=BinaryNode(24,parent=root.right)
    root.right.right=BinaryNode(32,parent=root.right)
    root.right.right.right=BinaryNode(33,parent=root.right.right)

    inOrder(root)

    successorNode=inOrderSuccessor(root)
    print("")
    print("successor of ",root, "is", successorNode)
    #print(successorNode.id) if successorNode else None

    successorNode = inOrderSuccessor(root.left)
    print("successor of ", root.left, "is", successorNode)

    successorNode = inOrderSuccessor(root.right)
    print("successor of ", root.right, "is", successorNode)

    successorNode = inOrderSuccessor(root.right.right.right)
    print("successor of ", root.right.right.right, "is", successorNode)

    successorNode = inOrderSuccessor(root.left.right.right)
    print("successor of ", root.left.right.right, "is", successorNode)

    successorNode = inOrderSuccessor(root.left.left.right)
    print("successor of ", root.left.left.right, "is", successorNode)

