from typing import List


def partition(arr: List, start: int, end: int) -> int:
    """Partition function using last element as pivot.

    Args:
        arr (list): The array to partition
        start (int): Starting index of subarray
        end (int): Ending index of subarray (pivot location)

    Returns:
        int: Final position of pivot after partitioning
    """
    pivot_value = arr[end]  # Choose last element as pivot
    i = start - 1  # Index of smaller element

    # Traverse through start to end-1
    for j in range(start, end):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def sort(arr: List, start: int, end: int) -> None:
    """QuickSort Algorithm

    Args:
        arr (list): The array to sort
        start (int): Starting index
        end (int): Ending index

    Return:
        None (because sorts in-place)
    """
    if start < end:
        # Partition the array and get pivot index
        pivot_index = partition(arr, start, end)

        # Recursively sort elements before and after partition
        sort(arr, start, pivot_index - 1)
        sort(arr, pivot_index + 1, end)


def quick_sort(arr: List) -> List:
    """Public interface for QuickSort
    Args:
        arr (list): The array to sort
    Returns:
        list: A new sorted array (doesn't modify original)
    """
    if not arr:  # Handle empty array
        return []

    # Make a copy to avoid modifying the original array
    result = arr.copy()

    # Sort the copy in-place
    sort(result, 0, len(result) - 1)

    return result
