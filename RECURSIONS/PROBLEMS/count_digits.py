class Solution:
    def countDigits(self, n):
        if n == 0:
            return 0
        return (n//n) + self.countDigits(n//10)