# Nickname Generator

# Write a function, nicknameGenerator that takes a string name as an argument 
# and returns the first 3 or 4 letters as a nickname.

# If the 3rd letter is a consonant, return the first 3 letters.
# nickname("Robert") //=> "Rob"
# nickname("Kimberly") //=> "Kim"
# nickname("Samantha") //=> "Sam"

# If the 3rd letter is a vowel, return the first 4 letters.
# nickname("Jeannie") //=> "Jean"
# nickname("Douglas") //=> "Doug"
# nickname("Gregory") //=> "Greg"

# If the string is less than 4 characters, return "Error: Name too short".
# nickname("Dan") //=> "Error: Name too short"
# nickname("Ed") //=> "Error: Name too short"
# nickname("Meg") //=> "Error: Name too short"

# Notes:
# Vowels are "aeiou", so discount the letter "y".
# Input will always be a string.
# Input will always have the first letter capitalized and the rest lowercase (e.g. Sam).


def solution(name):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    # vowels = 'aeiou'
    if len(name) < 4:
        return 'Error: Name too short'
    elif name[2] in vowels:
        return name[:4]
    else:
        return name[:3]
