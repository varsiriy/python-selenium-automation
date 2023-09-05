string = "Placeholder 1: {}, Placeholder 2: {}"

print("is" in string)    # return true/false

print(string[0]) #or [-1], [:4], [1:4], [0:10:2]

print(string + "plus something extra")   # concatenation

print(len(string))  # length of the string

print(string.lower)  # or string.uppper

print(string.split()) # splits each word

print(string.split("t"))  # splits by letter "t"

print("t".join(string))  # add "t" to the string

print(string.strip())   # remove empty spaces

print(string.strip(".")) # remove "." if available

print(string.replace(".", "+"))  # replace "." with "+"

print(string.find("i"))  # find numerous location. If not find returns -1

print(string.format(123, "string"))   # formats {} {} in string


def reverse_string(s: str):     # reverse string
    print(s[::-1])

reverse_string("ABCDE")


def reverse_number(number: int):    # reverse number with "-"
    string = str(number)
    if string[0] == "-":
        return int("-" + string[:0:-1])
    else:
        return int(string[::-1])

print(reverse_number(-678))
print(reverse_number(678))


def is_anagram(s1: str, s2: str):     # Anagram
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

print(is_anagram("cat", "act"))  # true
print(is_anagram("cat", "ace"))  # false
print(is_anagram("cat", "actt"))  # false


def is_palindrome(s: str):    # Palindrome
    if s == s[::-1]:
        return True
    else:
        return False

print(is_palindrome("madam"))  # true
print(is_palindrome("common"))  # false


def almost_palindrome(s: str):     # almost palindrome. If remove one letter become a palindrome
    word = len(s)
    for i in range(word):
        new_s = s[:i] + s[i + 1:]
        if new_s == new_s[::-1]:
            return True
    return False


print(almost_palindrome("rakdar"))
print(almost_palindrome("rakidar"))



