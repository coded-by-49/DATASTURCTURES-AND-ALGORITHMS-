def palindrome_check(n):
    copy = n
    reverse_num = 0
    ld = 0
    while n>0:
        ld = n % 10 # we want to return the remainder because that is the last digit
        reverse_num = reverse_num * 10 + ld
        n = n // 10 # we remove the last digit we just picked out
    return copy == reverse_num

print(palindrome_check(9))

def isPalindrome(self, x: int) -> bool:
        # If x is a negative number it is not a palindrome
        # If x % 10 = 0, in order for it to be a palindrome the first digit should also be 0
        if x < 0 or (x > 0 and x%10 == 0):   
            return False

        reversedNum = 0
        while x > reversedNum:
            reversedNum = reversedNum * 10 + x % 10
            x = x // 10

        # If x is equal to reversed number then it is a palindrome
        # If x has odd number of digits, dicard the middle digit before comparing with x
        # Example, if x = 23132, at the end of for loop x = 23 and reversedNum = 231
        # So, reversedNum/10 = 23, which is equal to x
        return True if (x == reversedNum or x == reversedNum // 10) else False
        
