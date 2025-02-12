import sys

"""
I/P:
str (main): ADOBECODEBANC
str (conditional str): ABC

O/P:
BANC
"""

main_str = "ADOBECODEBANC"
conditional_str = "ABC"
char_counter = {}
i = 0
j = 0
shortest = sys.maxsize
ans = None
while i < len(main_str) or j < len(main_str):
    if len(char_counter) < len(conditional_str):
        if j < len(main_str):
            if main_str[j] in conditional_str and main_str[j] in char_counter:
                char_counter[main_str[j]] += 1
            elif main_str[j] in conditional_str and main_str[j] not in char_counter:
                char_counter[main_str[j]] = 1
            j += 1
        else:
            break
    elif len(char_counter) == len(conditional_str):
        if shortest > j - i + 1:
            shortest = j - i + 1
            ans = main_str[i : j + 1]
        if i < j:
            if (
                main_str[i] in conditional_str
                and main_str[i] in char_counter
                and char_counter[main_str[i]] - 1 > 0
            ):
                char_counter[main_str[i]] -= 1
            elif (
                main_str[i] in conditional_str
                and main_str[i] in char_counter
                and char_counter[main_str[i]] - 1 == 0
            ):
                del char_counter[main_str[i]]

            i += 1
        else:
            if main_str[j] in conditional_str and main_str[j] in char_counter:
                char_counter[main_str[j]] += 1
            elif main_str[j] in conditional_str and main_str[j] not in char_counter:
                char_counter[main_str[j]] = 1
            j += 1
    else:
        if i < j:
            if (
                main_str[i] in conditional_str
                and main_str[i] in char_counter
                and char_counter[main_str[i]] - 1 > 0
            ):
                char_counter[main_str[i]] -= 1
            elif (
                main_str[i] in conditional_str
                and main_str[i] in char_counter
                and char_counter[main_str[i]] - 1 == 0
            ):
                del char_counter[main_str[i]]

            i += 1


print(ans)
