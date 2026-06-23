DEBUG: bool = True 

def bubble_sort_unoptimised(arr: list[int]) -> list[int]:
    """
        Unoptimised bubble sort that sorts array of integers in
        non-decreasing order
    """

    n = len(arr)

    # outer loop iterates n-1 passes over the array
    # each iteration puts one element into place
    # once n-1 items are in the right order, the last item must be in the right order too

    for pass_num in range(n - 1): 

        # inner loop swaps largest element to the end
        for i in range(n - 1):

            # swap adjacent elements if out of order
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

        if DEBUG:
            print(f"Iteration {pass_num}: {arr}")

    return arr


nums = [5, 2, 8, 1, 3]
print(f"Sorted array: {bubble_sort_unoptimised(nums)}")

