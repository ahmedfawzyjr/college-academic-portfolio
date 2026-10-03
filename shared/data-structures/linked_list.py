"""
Singly & Doubly Linked List Data Structures
"""

from typing import Any, Optional, Iterator

class Node:
    def __init__(self, value: Any, next_node: Optional['Node'] = None):
        self.value = value
        self.next = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self._size = 0

    def append(self, value: Any):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def prepend(self, value: Any):
        new_node = Node(value, self.head)
        self.head = new_node
        self._size += 1

    def delete(self, value: Any) -> bool:
        if not self.head:
            return False
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return True
        curr = self.head
        while curr.next and curr.next.value != value:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
            self._size -= 1
            return True
        return False

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def to_list(self) -> list:
        res = []
        curr = self.head
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next
