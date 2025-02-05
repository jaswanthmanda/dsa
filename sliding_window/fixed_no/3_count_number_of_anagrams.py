"""
BRUTE FORCE:

1. Count no of anangrams basic example
i/p string: for (check anagram)
i/p string: forxxorfxdorf
"""

input_string = "forxxorfxdorf"
check_anagram_string = "for"
K = len(check_anagram_string)
i = 0
j = 0

result = 0

counter = {}
match_counter = {}

for char in check_anagram_string:
    if char in match_counter:
        match_counter[char] += 1
    else:
        match_counter[char] = 1

# main logic
while j < len(input_string):
    if j - i + 1 < K:
        if input_string[j] in counter:
            counter[input_string[j]] += 1
        else:
            counter[input_string[j]] = 1
        j += 1
    elif j - i + 1 == K:
        if input_string[j] in counter:
            counter[input_string[j]] += 1
        else:
            counter[input_string[j]] = 1

        if counter == match_counter:
            result += 1

        if counter[input_string[i]] - 1 > 0:
            counter[input_string[i]] -= 1
        else:
            del counter[input_string[i]]

        i += 1
        j += 1

print(result)
print()
print()


"""
OPTIMIZED:

Input:
txt = aaba
pat = aaba
Output: 4
Explanation: aaba is present 4 times
in txt.
"""
input_string = "aabaabaa"
check_anagram_string = "aaba"
K = len(check_anagram_string)
i = 0
j = 0

result = 0

match_counter = {}

count = 0

for char in check_anagram_string:
    if char in match_counter:
        match_counter[char] += 1
    else:
        count += 1
        match_counter[char] = 1


# main logic
while j < len(input_string):

    if j - i + 1 < K:
        if input_string[j] in match_counter:
            match_counter[input_string[j]] -= 1
            if match_counter[input_string[j]] == 0:
                count -= 1
        j += 1

    elif j - i + 1 == K:
        if input_string[j] in match_counter:
            match_counter[input_string[j]] -= 1
            if match_counter[input_string[j]] == 0:
                count -= 1

        if count == 0:
            result += 1

        if input_string[i] in match_counter:
            match_counter[input_string[i]] += 1
            if match_counter[input_string[i]] == 1:
                count += 1

        i += 1
        j += 1

print(result)
print()
print()


"""
Optimized:

1. Count no of anangrams basic example
i/p string: for (check anagram)
i/p string: forxxorfxdorf
"""
input_string = "forxxorfxdor"
check_anagram_string = "for"
K = len(check_anagram_string)
i = 0
j = 0

result = 0

match_counter = {}

count = 0

for char in check_anagram_string:
    if char in match_counter:
        match_counter[char] += 1
    else:
        count += 1
        match_counter[char] = 1


# main logic
while j < len(input_string):

    if j - i + 1 < K:
        if input_string[j] in match_counter:
            match_counter[input_string[j]] -= 1
            if match_counter[input_string[j]] == 0:
                count -= 1
        j += 1

    elif j - i + 1 == K:
        if input_string[j] in match_counter:
            match_counter[input_string[j]] -= 1
            if match_counter[input_string[j]] == 0:
                count -= 1

        if count == 0:
            result += 1

        if input_string[i] in match_counter:
            match_counter[input_string[i]] += 1
            if match_counter[input_string[i]] == 1:
                count += 1

        i += 1
        j += 1

print(result)
