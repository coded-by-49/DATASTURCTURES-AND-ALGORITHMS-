def fib(n):
    # Base case 1: If n is 0, the 0th Fibonacci number is 0.
    if (n == 0):
        return 0
    # Base case 2: If n is 1, the 1st Fibonacci number is 1.
    if (n == 1):
        return 1
    # The function calls itself with smaller inputs (n-1 and n-2), moving closer to the base cases.
    return fib(n-1) + fib(n-2)
