def reverse_integer(n: int):
    string = str(n)
    if string[0] == "-":
        return int("-" + string[:0:-1])
    else:
        return int(string[::-1])

print(reverse_integer(-189))


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


def reverse_words(sentence: str):
    sentence = sentence.split()
    reverse_words = []
    for word in sentence:
        reverse_word = word[::-1]
        reverse_words.append(reverse_word)
    result = " ".join(reverse_words)
    return result

print(reverse_words("Hello World"))
print(reverse_words("mistertwister"))


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


def shortcut(s: str):
    vowels = "aeiuo"
    result = ""
    for char in s:
        if char not in vowels:
            result += char

    return result

print(shortcut("hello"))
print(shortcut("goodbye"))


