N = 142312
def countDigit(num):
    count = 0 
    while num > 0:
        count = count + 1
        num = num // 10
    return count

print(countDigit(N))