def alternating_case(text):
    alternated = []
    for i,value in enumerate(input_string):
        if i % 2 == 0 :
            value = value.capitalize()
            alternated.append(value)
        else : 
            alternated.append(value)
    return ''.join(alternated)

if __name__ == "__main__":
    input_string = input().strip()
    result = alternating_case(input_string)
    print(result)


#### LOGIC 
# input = input().strip()
# print(input)
# result=[]
# for i,value in enumerate(input):
#     if i % 2 == 0 :
#         value = value.capitalize()
#         result.append(value)
#     else:
#         result.append(value)

# print("".join(result))
