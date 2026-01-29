def bubble_sort(arr: list[int]) -> list[int]:
    """Bubble sort: a naive sorting algorithm that compares and swaps two adjacent values

    Args:
        arr (list): a non-sorted list of integers

    Returns:
        list: a sorted list of integers in increasing order
    """
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
