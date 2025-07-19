def filter_words(sentence, min_length):
    # TODO: Implement the function using a Generator expression
    return (word for word in sentence.split() if len(word) >= min_length)
            
            
        

if __name__ == "__main__":
    sentence = input().strip()
    min_length = int(input().strip())
    
    filtered_words = filter_words(sentence, min_length)
    print(list(filtered_words))


## LOGIC 
# sentence = "The quick brown fox jumps over the lazy dog"
# min_length = 4 
# print(sentence.split())
# for i,value in enumerate(sentence.split()) :
#     print(f"{value} : {len(value)}")
#     if len(value) >= min_length : 
#         pass 
    