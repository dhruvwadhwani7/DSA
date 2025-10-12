# Problem Statement: Given two integers N1 and N2, find their greatest common divisor.

# The Greatest Common Divisor of any two integers is the largest number that divides both integers.

# class Solution():
#     def greatestDivisor(self,num1,num2):
#         min_num = min(num1,num2)
#         gcd = 1
#         for i in range(1,min_num+1):
#             if num1 % i == 0 and num2 % i == 0:
#                 gcd = i
#         return gcd 
            
class Solution():
    def greatestDivisor(self,num1,num2):
        while num2 > 0 :
            num1 , num2 = num2 , num1 % num2 
        return num1 
        
        
        
        
sol = Solution()
print(sol.greatestDivisor(15,20))
print(sol.greatestDivisor(15,22))
print(sol.greatestDivisor(15,365))