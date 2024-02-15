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

class SortArrayUsingRecursion:

    def __init__(self) -> None:
        pass

    def insert_into_array(self, arr: list, item: int) -> list:
        """Inserts item into list for sorting"""
        if len(arr) == 1:
            if item <= arr[0]:
                arr.insert(0, item)
            elif item >= arr[0]:
                arr.append(item)
            return arr
        if item <= arr[-1]:
            new_item = arr[-1]
            arr = arr[:-1]
            self.insert_into_array(arr, item)
            arr.append(new_item)
        else:
            arr.append(item)

        return arr


    def sort_an_array_recu(self, arr: list) -> list:
        """Sorts an array using recursion"""
        # base case
        if len(arr) == 0 or len(arr) == 1:
            return arr

        # base logic
        item = arr[-1]
        arr = arr[:-1]
        arr = self.sort_an_array_recu(arr)
        if item <= arr[0]:
            arr.insert(0, item)
        elif item >= arr[-1]:
            arr.append(item)
        else:
            arr = self.insert_into_array(arr, item)
        return arr

class SortAStack:

    def __init__(self) -> None:
        """Initializer"""
        pass

    def insert_into_stack(self, stack: list, item: int) -> list:
        """Inserts a item into stack and returns stack"""
        if len(stack) == 0:
            stack.append(item)
            return stack
        if len(stack) == 1:
            if stack[-1] < item:
                new_item = stack.pop()
                stack.append(item)
                stack.append(new_item)
            else:
                stack.append(item)
            return stack

        if stack[-1] < item:
            new_item = stack.pop()
            self.insert_into_stack(stack, item)
            stack.append(new_item)
        else:
            stack.append(item)

        return stack

    def sort_a_stack(self, stack: list):
        """Sorts a given stack"""
        # base case
        if len(stack) in (0, 1):
            return stack

        # base logic
        new_item = stack.pop()
        stack = self.sort_a_stack(stack)

        if stack[-1] < new_item:
            stack = self.insert_into_stack(stack, new_item)
        else:
            stack.append(new_item)

        return stack

class gFseries:
    def gfSeries_suporter(self, count: int, arr: list) -> None:
        # code here
        if count <= 1:
            return arr
        elif len(arr) > count:
            return arr

        # base logic
        if count-1 >= len(arr) or count-2 >= len(arr):
            self.gfSeries_suporter(count-1, arr)
        temp = ((arr[count-2])**2) - (arr[count-1])
        arr.append(temp)
        return self.gfSeries_suporter(count-1, arr)

    def gfSeries(self, n:int) -> None:

        if n == 2:
            print(0, 1, end = " ")
        else:
            ans = [0, 1]

            ans = self.gfSeries_suporter(n-1, ans)
            print(*ans)





# function calls
# print(factorial(5))
# print(fibonacci_num(5))
# print_1_to_n(4)
# print_n_to_1(25)
# print(sum_of_numbers(25))
# print(recursive_palindrome("abbbba"))
# new_obj = SortArrayUsingRecursion()
# print(new_obj.sort_an_array_recu([2, 7, 1, 4, 3, 5, 6]))
# print(new_obj.sort_an_array_recu([2]))
# print(new_obj.sort_an_array_recu([1]))
# print(new_obj.sort_an_array_recu([1, 2, 3, 4, 5, 6, 7]))
# new_obj = SortAStack()
# print(new_obj.sort_a_stack([5, 1, 0, 2]))
# print(new_obj.sort_a_stack([2, 3, 1]))
# print(new_obj.sort_a_stack([3, 2, 1]))
new_obj = gFseries()
print(new_obj.gfSeries(13))