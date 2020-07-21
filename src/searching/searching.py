def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # $%$Start
    # if len(arr) == 0:
    #     return -1  # array empty
    # low = 0
    # high = len(arr)-1
    # while low <= high:
    #     middle = (low+high)//2
    #     if target < arr[middle]:
    #         high = middle - 1  # eliminate RHS
    #     elif target > arr[middle]:
    #         low = middle + 1  # eliminate LHS
    #     else:
    #         return middle
    # # $%$End
    # return -1 

    # if len(arr) == 0:
    #     return -1
    start = 0
    stop = len(arr)-1
    while start <= stop:
        mid = (start + stop)//2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            start = mid + 1
        else:
            stop = mid - 1
            

    return -1  # not found
