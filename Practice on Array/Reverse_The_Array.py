# We can reverse the array using in-built function

arrr = [5, 8, 6, 7, 3, 5, 4, 4]
print(len(arrr))
arrr.sort()
print(arrr)

# We can use slicing ton reverse the array

sl = [5, 9, 6, 3, 1, 4, 7]
print(sl[::-1])

# We can use  Iterative way to reverse the array


def rev(arr):
    starting_point = 0
    ending_point = len(A) - 1
    while starting_point < ending_point:
        arr[starting_point], arr[ending_point] = arr[ending_point], arr[starting_point]
        starting_point += 1
        ending_point -= 1
    print(arr)


A = [1, 2, 3, 4, 5, 6]
rev(A)


# We can use Recursive Way to reverse the array


def reverse(arr, starting_point, ending_point):

    if starting_point >= ending_point:
        return
    arr[starting_point], arr[ending_point] = arr[ending_point], arr[starting_point]
    reverse(arr, starting_point + 1, ending_point - 1)


arr = [5, 6, 8, 6, 3, 5]
starting_point = 0
ending_point = len(arr) - 1
reverse(arr, starting_point, ending_point)
print(arr)
