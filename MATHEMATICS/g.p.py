# def termOfGP(self,A,B,N):
#         if N==1:
#             return A
#         r = B/A
#         for i in range(N-2):
#             r *= r
#         return A*r

# for i in range(1):
#      print("common")

def modInverse(a,m):
        return (m-1)/a
    
print(modInverse(6,34))