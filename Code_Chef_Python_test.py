# str = "Coding on CodeChef"
# for item in str.split() :
#     print(f"{item} - {len(item)}")
# print(f"{str} - {len(str)}")

# x = int(input())
# y = int(input())
# print(x+y)

# num = int(input("Enter the number : "))
# if(not(num>0)):
#     print("Heloo")
# else : 
#     print("NO")

# a,b,c = map(int,input().split())
# print(a,b,c)
# if a<b<c :
#     print("Increasing")

# tup = (1,31,12,12)
# tup[5] = 6
# print(tup)

# student_grades = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65, "Eva": 88, "John": 45}
# name = input()
# if name in student_grades :
#     print(student_grades[name])
# else : 
#     print("Not Found")

# data = [2,4,6,8,10]
# print(data[0] + data[3])

# nums = map(int,input().split())
# list_nums = list(nums)
# print(list_nums[0] * list_nums[2])

# num = int(input())
# fact = 1  
# i = 1
# while i<=num:
#     fact = fact * i
#     i += 1 
# print(fact) 

# n = int(input().strip())
# sum = 0 
# for i in range(1,n+1):
#     sum = sum + i

# print(sum)    



        
def calculate_power(base, exponent):
    return base ** exponent 
    
    
    
def main():
    base, exponent = map(int, input().split())
    result = calculate_power(base, exponent)
    print(result)


main()


def is_even(num):
    # Complete the function 
    return num % 2 == 0 

def main():
    # Complete the function 
    t = int(input())
    for _ in range(t):
        num = int(input())
        if is_even(num):
            print("Even")
        else : 
            print("Odd")
    

if __name__ == "__main__":
    main()

    
        

