
def _merge_sort(arr: list[int], left: int, right: int) -> None:
    """
        Sort the subarray arr[left:right+1] using merge sort,
        modifying the list in place

        (subarray is left...right inclusive)
    """

    # if there are at least 2 elements in the subarray
    if left < right:
        mid = (left + right) // 2

        _merge_sort(arr, _____, mid)
        _merge_sort(arr, ______, right)
        merge(arr, _______, ______, _______)


def merge(arr: list[int], left: int, mid: int, right: int) -> None:
    """
        Merge sorted subarrays arr[left:mid+1] and arr[mid+1:right+1] into
        one sorted subarray arr[left:right+1], modifying the list in place
    """

    temp = [0] * (__________) # create temporary array to write to
    i, j = left, mid+1
    k = 0

    while i <= _______ and j <= _______:
        if arr[i] <= arr[j]:
            temp[k] = _______
            i += ____
        else:
            temp[k] = ______
            j += _____
        k += 1

    while i <= ______:
        temp[k] = ______
        i += 1
        k += 1

    while j <= _______:
        temp[k] = ______
        j += 1
        k += 1
        
    # write temporary array back to original array
    for i in range(k):
        arr[________] = temp[i]


def merge_sort(arr: list[int]) -> None:
    """
        Sort an array of integers using merge sort,
        modifying the array in place
    """
    _merge_sort(arr, _______, ________)


nums = [7, 6, 2, 3, 4, 1, 10, 8, 5, 9]
merge_sort(nums) # sort in place

print(f"Sorted array: {nums}")