def selection_sort(arr: list[int]) -> list[int]:
    """Selection sort

    The algorithm sorts a list by comparing one item with the remaining items in the list
    and swap that item with the smallest one. Continue with the second item until the last one.

    Args:
        arr (list): An unsorted list of integers

    Returns:
        arr (list): A sorted array in increasing order
    """
    if not arr:
        return []

    # Make a copy to avoid modifying the original
    result = arr.copy()

    for i in range(len(result)):
        min_idx = i
        for j in range(i + 1, len(result)):
            if result[j] < result[min_idx]:
                min_idx = j

        result[i], result[min_idx] = result[min_idx], result[i]

    return result
