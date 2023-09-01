# HW 5.
# Amazon interview question:
# Create a function that will take a string as an input
# and return the 1st unique letter of a string.
# "google" => l

# def unique(string:str):              #O(n^2) complexity
#     string = string.lower()  # google
#
#     for l in string:   #O(n)
#         if string.count(l) == 1:  # O(n)
#             return l

    # Or

def unique(string: str):                #O(n)
    string = string.lower()  # google

    d = {}
    for letter in string:   #O(n)
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] +=1
    #print(d)  # d = {'g': 2, 'o': 2, 'l': 1, 'e': 1 }

    for k, v in d.items():   #O(n)
        if v == 1:
            return k

print(unique('google'))
print(unique('Google'))
print(unique(''))
print(unique('gogo'))



# # Or if the task says PRINT the 1st unique letter. than:
#
#   for k, v in d.items():
#       if v == 1:
#           print(k)
#           return