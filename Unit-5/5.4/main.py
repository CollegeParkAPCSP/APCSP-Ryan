# using isalnum isalpha isdigit islower isupper

def find_sub(str, substr):
    if str.find(substr) == -1:
        print("Substring is not in string")
        return -1
    
    print(f"\nThe substring was found at character {str.find(substr) + 1}")
    
    print(f"all alphanumeric? {substr.isalnum()}")
    print(f"all alphabetic? {substr.isalpha()}")
    print(f"all digits? {substr.isdigit()}")
    print(f"all lowercase? {substr.islower()}")
    print(f"all uppercase? {substr.isupper()}\n")

find_sub("hello", "lo")