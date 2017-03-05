# First Common Ancestor with parent node connection
# search like a linkedlist

import sys
import treeLib


# sys.path.insert(0,"treeLib")


def firstCommonAncestor(node1, node2):
    depth1 = findDepth(node1)
    if depth1 < 1:
        return node1

    depth2 = findDepth(node2)
    if depth2 < 1:
        return node2

    if depth1 < depth2:
        deeperNode = node2
        shallowNode = node1
        diff = depth2 - depth1
    else:
        deeperNode=node1
        shallowNode=node2
        diff = depth1 - depth2

    for i in range(diff):
        deeperNode = deeperNode.parent

    while deeperNode is not shallowNode:
        deeperNode = deeperNode.parent
        shallowNode = shallowNode.parent
    return deeperNode


def findDepth(nodePtr):
    if not nodePtr:
        return -1
    return 1 + findDepth(nodePtr.parent)


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
