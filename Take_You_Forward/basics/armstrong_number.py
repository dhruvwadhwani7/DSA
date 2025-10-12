# Problem Statement: Given an integer N, return true it is an Armstrong number otherwise return false.

# An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

class Solution:
    def isArmstrong(self,n):
        length = len(str(n))
        sum = 0
        num = n
        while num>0:
            lastDigit = num % 10
            sum = sum + (lastDigit ** length)
            num = num // 10
        return sum == n

sol = Solution()
print(sol.isArmstrong(153))
        
