"""
Unit Tests for Shared Algorithms and Data Structures
"""

import unittest
from sorting import quick_sort, merge_sort, insertion_sort
from searching import binary_search, lower_bound
from graph_algorithms import Graph
from dynamic_programming import knapsack_01, longest_common_subsequence
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'data-structures'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utilities'))
from linked_list import SinglyLinkedList
from binary_search_tree import BinarySearchTree
from math_utils import is_prime, gcd, lcm, luhn_checksum

class TestSharedLibrary(unittest.TestCase):
    def test_sorting(self):
        data = [64, 34, 25, 12, 22, 11, 90]
        expected = sorted(data)
        self.assertEqual(quick_sort(data), expected)
        self.assertEqual(merge_sort(data), expected)
        self.assertEqual(insertion_sort(data), expected)

    def test_searching(self):
        data = [10, 20, 30, 40, 50, 60]
        self.assertEqual(binary_search(data, 30), 2)
        self.assertIsNone(binary_search(data, 25))
        self.assertEqual(lower_bound(data, 25), 2)

    def test_graph(self):
        g = Graph(directed=False)
        g.add_edge("A", "B", 4)
        g.add_edge("A", "C", 2)
        g.add_edge("C", "B", 1)
        g.add_edge("B", "D", 5)
        dists, _ = g.dijkstra("A")
        self.assertEqual(dists["B"], 3)  # A -> C -> B
        self.assertEqual(dists["D"], 8)

    def test_dp(self):
        val, chosen = knapsack_01([2, 3, 4, 5], [3, 4, 5, 6], 5)
        self.assertEqual(val, 7)  # items 0 and 1: weights 2+3=5, vals 3+4=7
        self.assertEqual(longest_common_subsequence("ABCBDAB", "BDCAB"), "BCAB")

    def test_linked_list(self):
        ll = SinglyLinkedList()
        ll.append(10)
        ll.append(20)
        ll.prepend(5)
        self.assertEqual(ll.to_list(), [5, 10, 20])
        ll.reverse()
        self.assertEqual(ll.to_list(), [20, 10, 5])
        self.assertTrue(ll.delete(10))
        self.assertEqual(ll.to_list(), [20, 5])

    def test_bst(self):
        bst = BinarySearchTree()
        for x in [50, 30, 70, 20, 40, 60, 80]:
            bst.insert(x)
        self.assertEqual(bst.inorder(), [20, 30, 40, 50, 60, 70, 80])
        self.assertEqual(bst.search(40), 40)
        self.assertIsNone(bst.search(99))

    def test_math(self):
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(18))
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(lcm(12, 18), 36)
        self.assertTrue(luhn_checksum("49927398716"))
        self.assertFalse(luhn_checksum("49927398717"))

if __name__ == '__main__':
    unittest.main()
