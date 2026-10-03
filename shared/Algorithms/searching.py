"""
Core Searching Algorithms Library
Binary search and bounds lookup.
"""

from typing import List, Any, Optional

def binary_search(arr: List[Any], target: Any) -> Optional[int]:
    """Returns the index of target in a sorted list, or None if not found."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

def lower_bound(arr: List[Any], target: Any) -> int:
    """Returns the first index where arr[i] >= target."""
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low
