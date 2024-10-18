def concatenate_and_length(str1, str2):
    return len(str1 + str2)

print(concatenate_and_length("Hello", "World"))
print("\n")

def slice_and_length(phrase: str):
    words = phrase.split(" ")
    count = 0
    
    for i in range(len(words)):
        count += len(words[i])
    
    return count
    
result_length2 = slice_and_length("Python Programming") # 17
print("Length of Concatenated String:", result_length2)
print("\n")

def concatenate_substrings(text):
    if (len(text) < 10):
        return len(text)
    
    return len(text[:4] + text[-6:])

result_length3 = concatenate_substrings("Oh Man I love Python!")
print("Length of Concatenated Substrings:", result_length3) # 10
print("\n")

def remove_and_concatenate(sentence: str):
    i = sentence.find("is")
    
    sentence = sentence[:i] + sentence[i + 2:]
    return len(sentence)

result_length4 = remove_and_concatenate("This is an example")
print("Length of Concatenated Substrings:", result_length4) # 16
print("This includes spaces also because i didn't realize we were meant to write a case-specific function :(")
print("\n")

def extract_and_length(word):
    if (len(word) < 5):
        return word
    
    return len(word[:4] + word[-5:])

result_length5 = extract_and_length("Power Overwhelming!")
print("Length of Concatenated Substrings:", result_length5)
print("\n")