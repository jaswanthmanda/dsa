def factorial(n: int) -> int:
    """Return factorial"""
    if n==1:
        return n
    return n * factorial(n-1)

def fibonacci_num(n: int) -> int:
    """Fibonacci num"""
    if n == 0  or n == 1:
        return n
    return fibonacci_num(n-1) + fibonacci_num(n-2)

def print_1_to_n(n: int) -> None:
    """Prints 1 to N using recursion"""
    if n == 0:
        return
    print_1_to_n(n-1)
    print(n)

def print_n_to_1(n: int) -> None:
    """Prints N to 1 using recursion"""
    if n == 0:
        return
    print(n)
    print_n_to_1(n-1)

def sum_of_numbers(n: int) -> None:
    """Returns sum of digits using recursion"""
    if n < 1:
        return 0
    return n%10 + sum_of_numbers(n//10)

def recursive_palindrome(charti: str) -> bool:
    """Says if string is palindrome or not recursively"""
    if len(charti) == 2 and charti[0] == charti[1]:
        return True
    elif len(charti) == 2 and charti[0] != charti[1]:
        return False
    elif len(charti) == 1:
        return True
    return recursive_palindrome(charti[1:-1]) if charti[0] == charti[-1] else False

# function calls
# print(factorial(5))
# print(fibonacci_num(5))
# print_1_to_n(4)
# print_n_to_1(25)
# print(sum_of_numbers(25))
print(recursive_palindrome("abbbba"))