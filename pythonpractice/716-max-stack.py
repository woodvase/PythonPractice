from sortedcontainers import SortedList, SortedSet

from pythonpractice.double_linked_node import DoubleLinkedNode


class Solution:
    def __init__(self):
        self.__head = DoubleLinkedNode(0)
        self.__tail = DoubleLinkedNode(0)
        self.__head.next = self.__tail
        self.__tail.pre = self.__head
        # SortedList without key function doesn't work even there is a __lt__ function in the DoubleLinkedNode
        self.__sortedList = SortedList(key=lambda x: x.value)

    def push(self, x: int) -> None:
        newNode = DoubleLinkedNode(x)
        self.__tail.pre.next = newNode
        newNode.pre = self.__tail.pre
        newNode.next = self.__tail
        self.__tail.pre = newNode
        self.__sortedList.add(newNode)

    def pop(self) -> int:
        n = self.__tail.pre
        if n is not self.__head:
            self.__sortedList.remove(n)
            n.pre.next = self.__tail
            self.__tail.pre = n.pre
            return n.value

    def top(self) -> int:
        if self.__tail.pre is not self.__head:
            return self.__tail.pre.value

    def peekMax(self) -> int:
        l = len(self.__sortedList)
        if l > 0:
            return self.__sortedList[l - 1].value

    def popMax(self) -> int:
        l = len(self.__sortedList)
        if l > 0:
            maxNode = self.__sortedList[l - 1]
            self.__sortedList.remove(maxNode)
            maxNode.pre.next = maxNode.next
            maxNode.next.pre = maxNode.pre
            return maxNode.value


stk = Solution()
stk.push(5)  # [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.push(1)  # [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5)  # [5] the top of the stack and the maximum number is 5.
print(stk.popMax())  # return 5, [5, 1] the stack is changed now, and the top is different from the max.
print(stk.peekMax())  # return 5, [5, 1] the stack is changed now, and the top is different from the max.
print(stk.pop())  # return 5, [5, 1] the stack is changed now, and the top is different from the max.
# print(stk.pop())  # return 5, [5, 1] the stack is changed now, and the top is different from the max.

# print(stk.top())  # return 5, [5, 1, 5] the stack did not change.
# print(stk.peekMax())  # return 5, [5, 1] the stack did not change.
# print(stk.popMax())  # return 5, [5, 1] the stack is changed now, and the top is different from the max.
# print(stk.popMax())  # return 5, [5, 1] the stack is changed now, and the top is different from the max.
# print(stk.top())  # return 5, [5, 1] the stack is changed now, and the top is different from the max.
# print(stk.top())  # return 1, [5, 1] the stack did not change.
# print(stk.pop())  # return 1, [5] the top of the stack and the max element is now 5.
# print(stk.top())  # return 5, [5] the stack did not change.
