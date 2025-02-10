"""
I/P:
str: pwwkew

O/P:
3
"""

i = 0
j = 0
st = "pwwkew"
unique_chars_set = set()
longest = -1
while j < len(st):
    if st[j] not in unique_chars_set:
        unique_chars_set.add(st[j])
        j += 1
    else:
        if longest < len(unique_chars_set):
            longest = len(unique_chars_set)
        while st[i] in unique_chars_set:
            unique_chars_set.remove(st[i])
            i += 1
print(longest)
