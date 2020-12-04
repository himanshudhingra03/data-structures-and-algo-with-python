# Insertion Sort
# Time Complexity - Worst case - O(n^2) for comparisons and swaping, best case-O(n) for comparisons and O(1) for swapping


def sort(arr):

    for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and current_element < arr[i]:
            arr[j + 1] = arr[i]
            j = j - 1
        arr[j + 1] = current_element


arr = [2, 5, 8, 4, 7, 1, 3, 6, 9]
sort(arr)
print(arr)
