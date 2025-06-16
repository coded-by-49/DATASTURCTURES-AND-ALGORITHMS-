class Solution:
    def isPrime(self,N):
        if N <= 1:
            return False 
        if (N%2 == 0 or N%3 == 0):
            if (N == 2 or N ==3):
                return True
            return False
        i = 5
        while (i*i <= N): # we looping throught the fundamental factors only
            if (N % i == 0 or N % (i+2) == 0):
                print(f"by {i} or {i+2}")
                return False
            i += 5
        return True
            
sol = Solution() 

print(sol.isPrime(989))