class Solution(object):
    def isPalindrome(self, x):
        if (str(x))[::-1] == str(x) : 
            return True
        else :
            return False 
        
        
# sol = Solution() 
# print(sol.isPalindrome(121))
# print(sol.isPalindrome(-121))
# print(sol.isPalindrome(10))
        
# x = 121
# str_x = str(x)
# if str_x[::-1] == str_x :
#     print(True)
# else : 
#     print(False)
    
# x = "Dhruv"
# print(x[::-1])



# // More optimized version of this code 

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
    