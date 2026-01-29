def bubble_sort(arr: list[int]) -> list[int]:
    """Bubble sort: a naive sorting algorithm that compares and swaps two adjacent values

    Args:
        arr (list): a non-sorted list of integers

    Returns:
        list: a sorted list of integers in increasing order
    """
    n = len(arr)
    result = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result
