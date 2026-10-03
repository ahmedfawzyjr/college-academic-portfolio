import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'solution')))
from search_solution import bfs

def test_bfs():
    g = {'A': ['B', 'C'], 'C': ['D']}
    assert bfs(g, 'A', 'D') == ['A', 'C', 'D']
    print('AI Assignment 01 Test Passed!')

if __name__ == '__main__':
    test_bfs()
