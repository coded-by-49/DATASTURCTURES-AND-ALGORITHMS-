#median(): It takes the array and its size N as parameters and returns the median as an integer.

def median(A,N):
    A.sort() # sort the list out
    if (N & 1 == 0): # check whether it has an even length
        return (A[N//2] + A[(N//2) - 1]) // 2 # sum the elements in the middle
    else:
        return A[N//2] # return the single element in the middle
        
def mean(A,N):
    # mean(): It takes the array and its size N as parameters and returns the mean as an integer.
    sum(A) # sum the list
    return sum(A)//N # divide it by the length

            
        