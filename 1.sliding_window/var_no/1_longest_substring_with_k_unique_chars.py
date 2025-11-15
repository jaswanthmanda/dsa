"""
I/P:
str: aabacbebebe
k: 3

O/P:
7

I/P:
str: aaaa
k = 2

O/P:
-1

I/P:
str: aabaaab
k = 2

O/P:
7
"""

st = "aabacbebebe"
k = 3
unique_map = {}

# problem of variable k size but sliding window problem because
# of k
i = 0
j = 0
counter = 0
longest = -1
unique_char = 0
while j < len(st):
    if unique_char < k:
        if st[j] in unique_map:
            unique_map[st[j]] += 1
        else:
            unique_map[st[j]] = 1
            unique_char += 1
        j += 1
    elif unique_char == k:
        if longest < j - i + 1:
            longest = j - i + 1

        if st[j] in unique_map:
            unique_map[st[j]] += 1
        else:
            unique_map[st[j]] = 1
            unique_char += 1

        j += 1
    else:
        while i < j and unique_char > k:
            if st[i] in unique_map and unique_map[st[i]] - 1 > 0:
                unique_map[st[i]] -= 1
            elif st[i] in unique_map and unique_map[st[i]] - 1 == 0:
                del unique_map[st[i]]
                unique_char -= 1
            i += 1

print(longest)
