# Selection Sort using python
# Time Complexity - O(n^2)


def sort(arr):
    size = len(arr)
    for i in range(size - 1):  # Save the one iteration
        min_index = i
        for j in range(min_index + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [2, 6, 9, 4, 3, 8, 3, 9, 32, 521]
sort(arr)
print(arr)
