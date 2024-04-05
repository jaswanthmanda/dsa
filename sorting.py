# merge union sorted arr
# only one occurence of each element in the final list
arr1 = [2, 10, 20, 20]
arr2 = [3, 20, 40]

m = len(arr1)
n = len(arr2)

ind1 = 0
ind2 = 0
new_list = []
while ind1 < m and ind2 < n:
    if ind1 > 0 and arr1[ind1-1] == arr1[ind1]:
        ind1 += 1
    elif ind2 > 0 and arr2[ind2-1] == arr2[ind2]:
        ind2 += 1
    elif arr1[ind1] < arr2[ind2]:
        new_list.append(arr1[ind1])
        ind1 += 1
    elif arr1[ind1] > arr2[ind2]:
        new_list.append(arr2[ind2])
        ind2 += 1
    else:
        new_list.append(arr1[ind1])
        ind1 += 1
        ind2 += 1

while ind1 < m:
    if ind1 > 0 and arr1[ind1-1] != arr1[ind1]:
        new_list.append(arr1[ind1])
    ind1 += 1

while ind2 < n:
    if ind2 > 0 and arr2[ind2-1] != arr2[ind2]:
        new_list.append(arr2[ind2])
    ind2 += 1

print(new_list) # output: [2, 3, 10, 20, 40] (t.c: o(m+n))

# intersection of sorted lists
# new list with single occurence of repeated elem
arr1 = [1, 20, 20, 40, 60]
arr2 = [2, 20, 20, 20, 40]

ind1 = 0
ind2 = 0

m = len(arr1)
n = len(arr2)

inters_list = []

while ind1 < m and ind2 < n:
    if ind1 > 0 and arr1[ind1] == arr1[ind1-1]:
        ind1 += 1
    elif arr1[ind1] < arr2[ind2]:
        ind1 += 1
    elif arr2[ind2] < arr1[ind1]:
        ind2 += 1
    elif arr1[ind1] == arr2[ind2]:
        inters_list.append(arr1[ind1])
        ind1 += 1
        ind2 += 1

print(inters_list)  # output: [20, 40] (t.c: o(m+n))


def bubble_sort(arr):
    # Your code here
    """
    Compares with next element
    """
    swapped = True
    while swapped is True:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    return arr


def selection_sort(arr: list[int]) -> None:
    # Write your code here
    """
    (4) ([3] 2 1 5)
    {1} (3) ([2] 4 5)
    {1 2 3 4 5}
    """
    # logic: swap if prev is greater than curr
    N = len(arr)

    for i in range(N):
        min_ind = i

        for j in range(i, N):
            if arr[j] < arr[min_ind]:
                min_ind = j

        arr[i], arr[min_ind] = arr[min_ind], arr[i]


    return arr

def insertion_sort(arr: list[int]) -> None:
    """
    Sorts the array from first
    Iterates through each item in the array and inserts in the position
    in the order.
    """

    # return result
    return arr

# Test cases
print("Selection Sort!")
print(selection_sort([5, 3, 8, 1, 2]))  # Output: [1, 2, 3, 5, 8]
print(selection_sort([9, 0, 6, 3, 2]))  # Output: [0, 2, 3, 6, 9]
print(selection_sort([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(selection_sort([]))              # Output: []
print(selection_sort([5]))             # Output: [5]
print(selection_sort([5, 5, 5]))       # Output: [5, 5, 5]
print(selection_sort([1, 2, 3, 4, 5])) # Output: [1, 2, 3, 4, 5]
print(selection_sort([5, 4, 3, 2, 1])) # Output: [1, 2, 3, 4, 5]
print(selection_sort([5, 1, 2, 3, 4])) # Output: [1, 2, 3, 4, 5]




# Test cases
print("Bubble Sort!")
print(bubble_sort([5, 3, 8, 1, 2]))  # Output: [1, 2, 3, 5, 8]
print(bubble_sort([9, 0, 6, 3, 2]))  # Output: [0, 2, 3, 6, 9]
print(bubble_sort([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(bubble_sort([]))  # Output: []
print(bubble_sort([1]))  # Output: [1]
print(bubble_sort([5, 5, 5]))  # Output: [5, 5, 5]

# Test cases
print("Insertion Sort!")
arr = [3, 1, 4, 2]
print(insertion_sort(arr))  # Expected output: [1, 2, 3, 4]
arr = [1, 2, 3, 4]
print(insertion_sort(arr))  # Expected output: [1, 2, 3, 4]
arr = [4, 3, 2, 1]
print(insertion_sort(arr))  # Expected output: [1, 2, 3, 4]
arr = [3, 1, 4, 2, 2, 1]
print(insertion_sort(arr))  # Expected output: [1, 1, 2, 2, 3, 4]
arr = []
print(insertion_sort(arr))  # Expected output: []
arr = [1]
print(insertion_sort(arr))  # Expected output: [1]
arr = [i for i in range(100, 0, -1)]  # List containing numbers from 100 to 1 in reverse order
print(insertion_sort(arr))  # Expected output: [1, 2, 3, ..., 100]
