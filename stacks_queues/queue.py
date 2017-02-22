class Node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next

class myQueue:
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail

    def add(self,item=0):
        node=Node(item)
        if self.tail:
            self.tail.next=node
            self.tail=node
        else:
            self.head=self.tail=node

    def remove(self):
        if self.head:
            node=self.head
            self.head=self.head.next
            node.next=None
            if not self.head:
                self.tail=self.head
            return node
        else:
            return None

    def peek(self):
        if self.head:
            return self.head.value
        return None

    def isEmpty(self):
        if self.head:
            return False
        else:
            return True

    def __str__(self):
        mStr=""
        node=self.head
        while node:
            mStr += str(node.value) + " "
            node=node.next

        return mStr

if __name__ == '__main__':
    mQ=myQueue()

    print("empty") if mQ.isEmpty() else print(mQ)

    mQ.add(3)
    mQ.add(2)
    mQ.add(1)

    print("empty") if mQ.isEmpty() else print(mQ)

    print(mQ.peek())

    node = mQ.remove()
    print("removedNone:",node.value) if node else print("None")

    node = mQ.remove()
    print("removedNone:", node.value) if node else print("None")

    mQ.add(7)

    print("empty") if mQ.isEmpty() else print(mQ)

    node = mQ.remove()
    print("removedNone:", node.value) if node else print("None")

    node = mQ.remove()
    print("removedNone:", node.value) if node else print("None")

    node = mQ.remove()
    print("removedNone:", node.value) if node else print("None")


