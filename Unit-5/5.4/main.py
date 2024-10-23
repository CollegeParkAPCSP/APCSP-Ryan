def find_sub(string, substr):
    if string.find(substr) == -1:
        print("Substring is not in string")
        return -1
    
    print(f"\nThe substring was found at character {string.find(substr) + 1}")
    
    print(f"all alphanumeric? {string.isalnum()}")
    print(f"all alphabetic? {string.isalpha()}")
    print(f"all digits? {string.isdigit()}")
    print(f"all lowercase? {string.islower()}")
    print(f"all uppercase? {string.isupper()}\n")

find_sub("hello", "lo")