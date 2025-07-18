class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        digits = str(x)
        start = 0
        end = len(digits) - 1

        while start < end:
            if (digits[start] == digits[end]):
                start+=1
                end-=1
            else:
                return False
        return True