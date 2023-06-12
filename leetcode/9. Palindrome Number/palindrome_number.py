class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):   
            return False
    
        n = 0
        while x > n:
            n = 10 * n + x % 10
            x = x // 10
        
        return x == n or x == n // 10
