from typing import Optional


class DoubleLinkedNode:
    def __init__(
        self,
        value: int,
        pre: Optional["DoubleLinkedNode"] = None,
        next: Optional["DoubleLinkedNode"] = None,
    ):
        self.value = value
        self.pre = pre
        self.next = next

    def __lt__(self, other):
        return self.value < other.value
