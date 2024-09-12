class MyLinkedList:

    def __init__(self):
        self.head = LinkedListNode(0)
        self.tail = LinkedListNode(0)
        self.head.next = self.tail

    def get(self, index: int) -> int:
        node = self.head.next
        i = 0
        while i < index and node != self.tail:
            node = node.next
            i += 1

        return -1 if node == self.tail else node.val

    def addAtHead(self, val: int) -> None:
        node = LinkedListNode(val, self.head.next)
        self.head.next = node

    def addAtTail(self, val: int) -> None:
        node = self.head
        while node.next != self.tail:
            node = node.next
        node.next = LinkedListNode(val, self.tail)

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.head
        i = 0
        while i < index and node != self.tail:
            node = node.next
            i += 1
        if node != self.tail:
            newNode = LinkedListNode(val, node.next)
            node.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        node = self.head
        i = 0
        while i < index and node.next != self.tail:
            node = node.next
            i += 1
        if node.next != self.tail:
            node.next = node.next.next


class LinkedListNode:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next
