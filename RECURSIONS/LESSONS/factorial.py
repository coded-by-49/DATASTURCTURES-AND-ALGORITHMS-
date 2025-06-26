def fac(n):
    # Base case: If n is 0, the factorial is 1.
    # This is the stopping condition for the recursion.
    if n == 0:
        return 1
    # Recursive case: If n is greater than 0, the factorial of n is n multiplied by the factorial of (n-1).
    # The function calls itself with a smaller input (n-1), moving closer to the base case.
    return n * fac(n-1)

fac(3)