"""
Binary Search Tree (BST) Implementation
"""

from typing import Any, Optional, List

class BSTNode:
    def __init__(self, key: Any, val: Any = None):
        self.key = key
        self.val = val if val is not None else key
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None

class BinarySearchTree:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, key: Any, val: Any = None):
        if not self.root:
            self.root = BSTNode(key, val)
        else:
            self._insert_rec(self.root, key, val)

    def _insert_rec(self, node: BSTNode, key: Any, val: Any):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key, val)
            else:
                self._insert_rec(node.left, key, val)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key, val)
            else:
                self._insert_rec(node.right, key, val)
        else:
            node.val = val

    def search(self, key: Any) -> Optional[Any]:
        curr = self.root
        while curr:
            if key == curr.key:
                return curr.val
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def inorder(self) -> List[Any]:
        res = []
        def _inorder(node: Optional[BSTNode]):
            if node:
                _inorder(node.left)
                res.append(node.key)
                _inorder(node.right)
        _inorder(self.root)
        return res
