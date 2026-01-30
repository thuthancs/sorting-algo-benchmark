from typing import List


def parent(i: int) -> int:
    return (i - 1) // 2


def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * i + 2


def max_heapify(arr: List, i: int, heap_size: int) -> None:
    """Maintain the max-heap property"""
    l = left(i)
    r = right(i)
    largest = i

    if l < heap_size and arr[l] > arr[largest]:
        largest = l
    if r < heap_size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size)


def build_max_heap(arr: List) -> None:
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n)


def sort(arr: List) -> None:
    """HeapSort Algorithm (in-place)"""
    n = len(arr)
    build_max_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)


def heap_sort(arr: List) -> List:
    """Public interface for HeapSort that matches test expectations

    Args:
        arr (list): The array to sort
    Returns:
        list: A new sorted array (doesn't modify original)
    """
    if not arr:  # Handle empty array
        return []

    # Make a copy to avoid modifying the original array
    result = arr.copy()

    # Sort the copy in-place using your original algorithm
    sort(result)

    return result
