def insertion_sort(arr: list[int]) -> list[int]:
    """Insertion Sort Algorithm.

    The algorithm works by incrementally building the final sorted list one item at a time.
    It compares the items and insert an item to the right postion in the already sorted subarray.

    Args:
        arr (list): An unsorted list of integers

    Returns:
        arr (list): A sorted array in increasing order
    """
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr
