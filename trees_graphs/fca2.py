# First Common Ancestor without link to parents

import sys
import treeLib


# sys.path.insert(0,"treeLib")


def firstCommonAncestor(root, node1, node2):

    if not root or not subTreeHas(root,node1) or not subTreeHas(root,node2):
        return None

    else:
        return fcaHelper(root,node1,node2)


def fcaHelper(root,node1,node2):
    if root is node1:
        return node1
    elif root is node2:
        return node2

    isOnLeft1= subTreeHas(root.left,node1)
    isOnLeft2= subTreeHas(root.left,node2)

    if isOnLeft1 is not isOnLeft2:
        return root
    else:
        if isOnLeft1:
            return fcaHelper(root.left,node1,node2)
        else:
            return fcaHelper(root.right,node1,node2)


def subTreeHas(root,node1):
    if not root:
        return False
    if root is node1:
        return True
    return subTreeHas(root.left,node1) or subTreeHas(root.right,node1)


def inOrderP(nodePtr):
    if nodePtr:
        inOrderP(nodePtr.left)
        sys.stdout.write(str(nodePtr.id) + " ")
        inOrderP(nodePtr.right)


if __name__ == "__main__":
    root = treeLib.BinaryNode(16)
    root.left = treeLib.BinaryNode(8)

    root.left.left = treeLib.BinaryNode(5)
    root.left.right = treeLib.BinaryNode(11)
    root.left.left.left = treeLib.BinaryNode(3)
    root.left.left.right = treeLib.BinaryNode(6)

    root.left.right.right = treeLib.BinaryNode(14)

    root.right = treeLib.BinaryNode(25)
    root.right.left = treeLib.BinaryNode(24)
    root.right.right = treeLib.BinaryNode(32)
    root.right.right.right = treeLib.BinaryNode(33)

    inOrderP(root)

    node1 = root
    node2 = root.right.right.right

    node = firstCommonAncestor(root,node1, node2)
    print("")
    print("first common ancestor of ",node1 , " and ",node2, " is:",node)

    node1 = root.left.left.right
    node2 = root.left.right
    node = firstCommonAncestor(root, node1, node2)
    print("first common ancestor of ", node1, " and ", node2, " is:", node)

    node1 = root.right.right.right
    node2 = root.right.left
    node = firstCommonAncestor(root, node1, node2)
    print("first common ancestor of ", node1, " and ", node2, " is:", node)
