"""
I/P:
str: abaaccab
 - a (1 type of toy)
 - b (2nd type of toy) ...
k: 2

O/P:
5
"""

st = "abaaccab"
k = 2

i = 0
j = 0
char_counter = {}
unique_chars = 0
longest = -1
while j < len(st):
    if unique_chars < k:
        if st[j] in char_counter:
            char_counter[st[j]] += 1
        else:
            char_counter[st[j]] = 1
            unique_chars += 1
        j += 1
    elif unique_chars == k:
        if longest < j - i + 1:
            longest = j - i + 1
        if st[j] in char_counter:
            char_counter[st[j]] += 1
        else:
            char_counter[st[j]] = 1
            unique_chars += 1
        j += 1
    else:
        while i < j and st[i] in char_counter:
            if st[i] in char_counter and char_counter[st[i]] - 1 > 0:
                char_counter[st[i]] -= 1
            elif st[i] in char_counter and char_counter[st[i]] - 1 == 0:
                del char_counter[st[i]]
                unique_chars -= 1
            i += 1

print(longest)
