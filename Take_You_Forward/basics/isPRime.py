class Solution:
    def isPrime(self,num):
        count = 0
        for i in range(1,num+1):
            if num % i == 0:
                count = count + 1
        
        if count == 2:
            return True
        
        return False

sol = Solution()
print(sol.isPrime(10))
print(sol.isPrime(2))
print(sol.isPrime(7))