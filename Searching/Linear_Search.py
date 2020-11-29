# Linear Search
# Time Complexcity - O(n)


def linear(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print("Elemrnt found at", i)
            break
    else:
        print("Element not found")


arr = [5, 6, 8, 9, 3, 5]
key = 8
linear(arr, key)
