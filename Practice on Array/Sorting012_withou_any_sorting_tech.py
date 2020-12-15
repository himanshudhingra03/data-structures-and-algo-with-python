# Time complecity - O(n)


def sort(arr):
    l = m = 0
    h = len(arr) - 1
    while m <= h:
        if arr[m] == 0:
            arr[l], arr[m] = arr[m], arr[l]
            l += 1
            m += 1
        elif arr[m] == 1:
            m += 1
        elif arr[m] == 2:
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1


if __name__ == "__main__":
    arr = [1, 0, 2, 2, 1, 0, 1, 2, 0]
    sort(arr)
    print(arr)
