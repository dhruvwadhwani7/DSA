# class Solution:
#     def printNumber(self):
#         num = int(input())
#         return num
    
# sol = Solution()
# print(sol.printNumber())

# Problem Statement: Given an integer N, return the number of digits in N.
# N = 12345
# str_N = str(N)
# print(len(str(N)))


# brute force method
n = 1234513981938
count = 0 
while n > 0 :
    count = count + 1
    n = n // 10 
print(count)

