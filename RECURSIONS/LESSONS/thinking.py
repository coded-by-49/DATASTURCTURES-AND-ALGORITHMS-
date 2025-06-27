def fibonacci(self,n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            
            return self.fibonacci(n-1)+self.fibonacci(n-2)