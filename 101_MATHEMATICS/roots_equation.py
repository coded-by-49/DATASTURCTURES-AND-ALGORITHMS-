#User function Template for python3
from typing import List # carry out research on this later
import math
class Solution:
    def quadraticRoots(self, a : int, b : int , c:int ) -> List[int]:
        disc = (b*b)-(4*a*c)
        if ((disc))<0:
            return [-1]

        root_1 = (-b + math.isqrt(disc) / (2*a) )
        root_2 = (-b - math.isqrt(disc) / (2*a) )
        roots = [root_1 , root_2]
        return roots

sol = Solution()
print(sol.quadraticRoots(2,2,5))