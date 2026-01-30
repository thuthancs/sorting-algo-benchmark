def merge_sort(arr: list[int]) -> list[int]:
    if not arr:
        return []

    result = arr.copy()

    sort(result, 0, len(result) - 1)

    return result


def sort(arr: list[int], start: int, end: int) -> None:
    """
    - merge(): to merge two subarrays
    - divide the original array into 2 subarrays
        - if the len(subarr) == 1 -> return subarr
        - else: recur on the left and recur on the right
    """
    if start >= end:
        return arr
    else:
        mid = (start + end) // 2

        sort(arr, start, mid)
        sort(arr, mid + 1, end)

        merge(arr, start, mid, end)


def merge(arr: list[int], start: int, mid: int, end: int):
    n1 = mid - start + 1
    n2 = end - mid
    left = [0] * n1
    right = [0] * n2

    for i in range(n1):
        left[i] = arr[start + i]
    for j in range(n2):
        right[j] = arr[mid + j + 1]

    i, j = 0, 0
    k = start

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
