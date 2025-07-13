import math
# def exactly3Divisors(N):
#     if (N<=3):
#         return 0
#     else:
#         div_3 = 0
#         for n in range(4,N+1):
#             i = 1
#             div_num = 0
#             while (i*i<=n):
#                 if(n%i == 0):
#                     div_num += 1 #count the i as a factor
#                     if (i*i != n):
#                         div_num += 1 #count what mutplies i too
#                 i+=1
#             if div_num == 3:
#                 div_3 += 1
#         return div_3

class Solution:
    def checking_for_prime(self,N):
        if N==1:
            return False
        if (N==2 or N == 3):
            return True
        if (N%2 == 0 or N%3 == 0):
            return False        
        i = 5 
        while (i*i<=N):
            if (N%i == 0) or (N%(i+2) == 0) :
                return False
            i += 6
        return True
        
    def divisible_by_3(self,N):
        if N<=3:
            return 0
        div_3 = 0
        i = 2
        while(i*i <= N):
            if self.checking_for_prime(i):
                div_3 += 1
            i += 1
        return div_3
                
sol = Solution()

print(sol.divisible_by_3(30))