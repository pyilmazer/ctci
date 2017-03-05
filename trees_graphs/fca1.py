# First Common Ancestor with parent node connection
# search in the node's subtree than sibling

import sys
import treeLib


# sys.path.insert(0,"treeLib")

def hasNode(root,node):
    if not root:
        return False
    if root is node:
        return True
    return hasNode(root.left,node) or hasNode(root.right,node)



def firstCommonAncestor(node1, node2):

    if hasNode(node1,node2):
        return node1
    elif hasNode(node2,node1):
        return node2
    parent=node1.parent
    sibling=parent.left if node1 is parent.right else parent.right
    while not hasNode(sibling,node2):
        node=parent
        parent=parent.parent
        sibling=parent.left if node is parent.right else parent.right

    return parent


def inOrderP(nodePtr):
    if nodePtr:
        inOrderP(nodePtr.left)
        sys.stdout.write(str(nodePtr.id) + " ")
        inOrderP(nodePtr.right)


if __name__ == "__main__":
    root = treeLib.BinaryNodeWithParentLink(16)
    root.left = treeLib.BinaryNodeWithParentLink(8, parent=root)

    root.left.left = treeLib.BinaryNodeWithParentLink(5, parent=root.left)
    root.left.right = treeLib.BinaryNodeWithParentLink(11, parent=root.left)
    root.left.left.left = treeLib.BinaryNodeWithParentLink(3, parent=root.left.left)
    root.left.left.right = treeLib.BinaryNodeWithParentLink(6, parent=root.left.left)

    root.left.right.right = treeLib.BinaryNodeWithParentLink(14, parent=root.left.right)

    root.right = treeLib.BinaryNodeWithParentLink(25, parent=root)
    root.right.left = treeLib.BinaryNodeWithParentLink(24, parent=root.right)
    root.right.right = treeLib.BinaryNodeWithParentLink(32, parent=root.right)
    root.right.right.right = treeLib.BinaryNodeWithParentLink(33, parent=root.right.right)

    inOrderP(root)

    node1 = root
    node2 = root.right.right.right

    node = firstCommonAncestor(node1, node2)
    print("")
    print("first common ancestor of ",node1 , " and ",node2, " is:",node)

    node1 = root.left.left.right
    node2 = root.left.right
    node = firstCommonAncestor(node1, node2)
    print("first common ancestor of ", node1, " and ", node2, " is:", node)

    node1 = root.right.right.right
    node2 = root.right.left
    node = firstCommonAncestor(node1, node2)
    print("first common ancestor of ", node1, " and ", node2, " is:", node)

