def sum_N(n: int):
    # Base case: If n is 0 or 1, the sum is n itself. this alos helps protect agains infinite recursion with python
    if n <= 1:
        return n
    # Recursive case: If n is greater than 1, the sum of numbers up to n is the sum of numbers up to (n-1) plus n.
    # The function calls itself with a smaller input (n-1), gradually working towards the base case.
    else:
        return sum_N(n-1) + n