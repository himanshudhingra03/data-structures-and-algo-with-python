def binary_search_recursion(arr, key, left_index, right_index):
    if right_index < left_index:
        return -1
    mid = (left_index + right_index) // 2
    if arr[mid] == key:
        return mid
    if key > arr[mid]:
        left_index = mid + 1
    else:
        right_index = mid - 1
        return binary_search_recursion(arr,key,left_index,right_index)

if __name__ == "__main__":

    arr=[2,3,5,6,8,9,10,99]
    key=6
    left_index=0
    right_index=len(arr)-1
    index=binary_search_recursion(arr,key,left_index,right_index)
    print(f"Element found at {index}")
