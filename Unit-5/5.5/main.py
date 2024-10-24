def price_tag(item: str, price: float):
    barcode = item[-12:]
    
    if barcode[0] == barcode[11]:
        return(f"{item[:-12]} is a counterfeit")
    
    return (f"The price of {item[:-12]} is ${price}")
    
print(price_tag("socks012345543210", 5.99)) # socks is a counterfeit
print(price_tag("crackers154813564987", 1.15)) # the price of crackers is $1.15
print(price_tag("apple juice164875931246", 4.58)) # the price of apple juice is $4.58
print(price_tag("milk164812374681", 3.95)) # milk is a counterfeit
print(price_tag("xbox360s264859761278", 499.99) + "\n") # the price of xbox360s is $499.99

def alphanumeric_password(password: str):
    if len(password) >= 12 and password.isalpha():
        return 3
    
    if len(password) >= 12 and password.isalnum():
        return 4
    
    if len(password) >= 8 and password.isalpha():
        return 1
    
    if len(password) >= 8 and password.isalnum():
        return 2
    
    return 0
    
print(alphanumeric_password("Pass1234")) # 2
print(alphanumeric_password("Pass!234")) # 0 (contains '!') 
print(alphanumeric_password("Short1")) # 0 (less than 8 characters) 
print(alphanumeric_password("SecurePass9")) # 2
print(alphanumeric_password("InvalidChar123")) # 4
print(alphanumeric_password("InvalidCharacters")) # 3
print("\n")

def remove_middle(s: str):
    middle = len(s) // 2
    
    if len(s) % 2 == 0:
        return s[:middle - 1] + s[middle + 1:]
    
    return s[:middle] + s[middle + 1:]

print(remove_middle("coding")) # "cong" 
print(remove_middle("computer")) # "comter" 
print(remove_middle("hello")) # "helo" 
print(remove_middle("abcde")) # "abde" 
print(remove_middle("hello world")) # "helloworld" 
print(remove_middle("a")) # ""

def find_word_between(s: str, start: str, end: str):
    start_idx = s.find(start)
    end_idx = s.find(end)
    
    if start_idx == -1 or end_idx == -1:
        return ""
    
    return s[start_idx + len(start):end_idx]

print(find_word_between("I love Python programming!", "love", "programming")) # " Python " 
print(find_word_between("begin <data> end", "<", ">")) # "data" 
print(find_word_between("start middle end", "start", "end")) # " middle " 
print(find_word_between("no match here", "start", "end")) # "" 
print(find_word_between("oops > start", ">", "<")) # ""