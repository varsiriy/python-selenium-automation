 #  Reverse a negative integer and keep the negative sign at the beginning.
 # Example: -189 -> -981
def reverse_integer(n: int):
    string = str(n)
    if string[0] == "-":
        return int("-" + string[:0:-1])
    else:
        return int(string[::-1])

print(reverse_integer(-189))


 # Have two strings as input and returns True if they are anagrams of each other, and False otherwise.
def are_anagram(s1: str, s2: str):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True

print(are_anagram("race", "care"))
print(are_anagram("hEArt", "earth"))
print(are_anagram("rattle","battle"))


 # Given a sentence, reverse the order of characters in each word
def reverse_words(sentence: str):
    sentence = sentence.split()
    result = []
    for word in sentence:
        result.append(word[::-1])

    return " ".join(result)

print(reverse_words("Hello World"))
print(reverse_words("mistertwister"))


 # Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value
def repeat_digits(s: str):
    result = ""
    for char in s:
        if char.isdigit():
            current_num = int(char)
            repeated_char = char * current_num
            result += repeated_char
        else:
            result += char
    return result

print(repeat_digits("312"))
print(repeat_digits("102"))


 #  Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u) in a given string.
 # “y” is not considered a vowel for this task
def shortcut(s: str):
    vowels = "aeiuo"
    result = ""
    for char in s:
        if char not in vowels:
            result += char

    return result

print(shortcut("hello"))
print(shortcut("goodbye"))


