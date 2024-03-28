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
