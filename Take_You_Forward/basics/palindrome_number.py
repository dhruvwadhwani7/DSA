class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed = 0 
        while x > reversed :
            reversed = reversed * 10 + x % 10 
            x = x//10 
            
        return x == reversed or x == reversed // 10 
       
sol = Solution() 
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))