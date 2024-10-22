def is_same_size(str1, str2):
    if len(str1) < 4:
        str1 += "four"
    
    print(len(str1) == len(str2))
    return (len(str1) == len(str2))

is_same_size("hello", "howdy")
is_same_size("blah blah blah", "yapping")
is_same_size("Happy Halloween", "Boo")
is_same_size("October", "coolio")
is_same_size("cow", "holycow")

def replace_vowel(str: str):
    str = str.lower()
    
    str = str.replace("a", "4")
    str = str.replace("e", "3")
    str = str.replace("i", "1")
    str = str.replace("o", "0")
    str = str.replace("u", "5")
    
    print(str)
    return str
    
replace_vowel("The quick brown fox jumps over the lazy dog")
replace_vowel("Avid diva")
replace_vowel("Yo, Banana boy")
replace_vowel("Never odd or even")
replace_vowel("Was it a cat I saw?")

def upper_half(str: str):
    lower = str[:len(str)//2]
    upper = str[len(str)//2:]
    
    print(lower.upper() + upper.lower())
    return lower.upper() + upper.lower()

upper_half("HelloWorld")
upper_half("Python Programming")
upper_half("aBCDeFGHiJKLMNoPQRSTuVWXYZ")
upper_half("ExAmPlEs")
upper_half("NoNotesNoBloat")

def find_vowel(str, vowel):
    str = str.lower()
    vowel = vowel.lower()
    
    if str.find(vowel) == -1:
        print("Vowel not found")
        return -1
    
    print(str.find(vowel))
    return str.find(vowel)

find_vowel("hello", "e")
find_vowel("blahblahblah", "a")
find_vowel("Halloween", "o")
find_vowel("coolio", "i")
find_vowel("holycow", "o")