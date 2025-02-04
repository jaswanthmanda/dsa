arr = [12, -1, -7, 8, -15, 30, 16, 28]

# [-1, -7, ]
# 12 -1 -7 8 -15 30 16 28
#     i    j

N = len(arr)

k = 3

i = 0
j = 0

negative_vals = []
result = []

while j < N:
    # if j - i + 1< k
    if j - i + 1 < k:
        if arr[j] < 0:
            negative_vals.append(arr[j])
        j += 1
    elif j - i + 1 == k:
        if arr[j] < 0:
            negative_vals.append(arr[j])
        if len(negative_vals) > 0:
            result.append(negative_vals[0])
        if len(negative_vals) > 0 and arr[i] == negative_vals[0]:
            negative_vals.pop(0)

        i += 1
        j += 1


print(result)
