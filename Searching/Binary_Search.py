# Binary Search using Recursion
# Time complexity - O(logn)


def binary_search(arr, key):

    left_index = 0
    right_index = len(arr) - 1
    while left_index <= right_index:
        mid = (left_index + right_index) // 2
    
        if arr[mid] == key:
            return mid
        if key > arr[mid]:
            left_index = mid + 1
            
        else:
            right_index = mid - 1
    return -1


if __name__ == "__main__":
    arr = [2, 4, 5, 6, 9, 11, 25]
    key = 5
    index = binary_search(arr, key)
    print(f"Number found at {index}")
