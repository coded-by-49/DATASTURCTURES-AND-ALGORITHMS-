class Solution:
    def isPalin(self,N):
        str_N = str(N)
        start,end = 0, len(str_N)-1
        while start < end:
            if str_N[start] != str_N[end]:
                return False
            start += 1
            end -=1
        return True