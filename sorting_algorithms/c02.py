DEBUG: bool = False 


def bubble_sort_optimised(arr: list[int]) -> list[int]:
    """
        Optimised bubble sort that sorts array of integers in
        non-decreasing order
    """

    n = len(arr)
    num_comparisons: int = 0
    
    # outer loop iterates n-1 passes over the array
    # each iteration puts one element into place like before

    for i in range(n - 1):

        # OPTIMISATION 1
        # if no swaps are made, the list is sorted

        swapped = ______ 

        # OPTIMIATION 2
        # sorted list builds from the TOP DOWN so we have one less element to check each time
        # at iteration i, we have i elements that are sorted at the end of the list

        for j in range(0, n - ________):

            num_comparisons += 1
            
            # swap adjacent elements if out of order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = _______ 

        # stops early if no swaps are made
        if swapped == ________:
            break

        if DEBUG:
            print(f"Iteration {i}: {arr}")
    
    if DEBUG:
        print(f"No. of comparisons = {num_comparisons}")

    return arr


nums = [7, 6, 2, 3, 4, 1, 10, 8, 5, 9]
print(f"Sorted array: {bubble_sort_optimised(nums)}")

