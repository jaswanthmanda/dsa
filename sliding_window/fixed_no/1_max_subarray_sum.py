# MAX sub array sum

# list
arr = [100, 200, 300, 400]
# 100 200 300 400
# i    j = 300
#      i    j = 500
#           i   j = 700

# k
k = 2

# get the max sub array sum for the given window
i = 0
j = 0

sum_ = 0
mx_ = 0

while j < len(arr):
    if j - i + 1 < k:
        sum_ += arr[j]
        j += 1
    elif j - i + 1 == k:
        sum_ += arr[j]
        mx_ = max(mx_, sum_)
        sum_ -= arr[i]
        i += 1
        j += 1

print(mx_)
