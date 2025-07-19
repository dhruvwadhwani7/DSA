# def reverse_strings(string_list):
#     # TODO: Implement a lambda function to reverse a string
#     # and use map() to apply it to all strings in the list
#     pass

# if __name__ == "__main__":
#     # Read input from stdin
#     input_strings = input().split()
    
#     # Call the reverse_strings function
#     reversed_strings = reverse_strings(input_strings)
    
#     # Print the result
#     print(" ".join(reversed_strings))


str = "Hello Hii"
for word in str :
    reversal = lambda word:word[::-1]

print(reversal(str))
