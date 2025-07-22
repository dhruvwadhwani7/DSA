# Problem Statement: Given an integer N return the reverse of the given number.
# Note: If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

n = 123450  
reversedNum = 0 
while n > 0 :
    ld = n % 10 
    reversedNum = ( reversedNum * 10 ) + ld 
    n = n// 10
print(reversedNum) 
        
