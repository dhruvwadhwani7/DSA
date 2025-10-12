# Problem Statement: Given an integer N, return all divisors of N.

# A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.

class Solution:
    def allDivisors(self,num):
        divisors = []
        for i in range(1,num+1):
            if num % i == 0:
                divisors.append(i)
        return divisors
sol = Solution()
print(sol.allDivisors(36))