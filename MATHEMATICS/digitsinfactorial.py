#User function Template for python3

class Solution:
    def digitsInFactorial(self,N):
        if (N<0):
            return "invalid input"
        if (N == 0 or N == 1):
            fact = 1
            return 1
        else:
            fact = 1
            for i in range(2,N+1):
                fact *= i
                print(fact)
                
            numbers = 0
            while (fact != 0): # the lowest number from a floor div is 0
                fact = fact//10
                numbers += 1
            return numbers
                
            
            

Sol1 = Solution()
print(Sol1.digitsInFactorial(5))