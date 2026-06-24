
def merge_sort(arr: list[int]) -> list[int]:
    """
        Sorts an array of integers in non-decreasing order
        using merge sort

        Time complexity: O(n logn)
    """

    # base case
    if len(arr) <= 1:
        return arr

    # divide the array into two halves
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]

    # DIVIDE
    left = merge_sort(left)
    right = merge_sort(right)

    # CONQUER
    return merge(left, right)


def merge(left: list[int], right: list[int]) -> list[int]:
    """
        Merges two arrays sorted in non-decreasing order
        into one array in non-decreasing order

        Time complexity: O(n)
    """
    res = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        # compare head of two lists and take the smaller one
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    # in the case there are remaining elements in left
    while i < len(left):
        res.append(left[i])
        i += 1

    # in the case there are remaining elements in right
    while j < len(right):
        res.append(right[j])
        j += 1

    return res


nums = [7, 6, 2, 3, 4, 1, 10, 8, 5, 9]
print(f"Sorted array: {merge_sort(nums)}")