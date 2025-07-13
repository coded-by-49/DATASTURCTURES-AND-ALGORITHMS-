class Solution:
    def printArrayRecursively(self,arr,n):
        if n<1: # base case 
            return 0 
        self.printArrayRecursively(arr,n-1) # our compiler stops here and recursion takes place until it reaches the base case , and then it unwinds
        print(arr[n-1], end = " ")
        