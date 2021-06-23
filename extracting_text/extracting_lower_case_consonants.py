# Extract lower case consonants from a text using the function list
from string import ascii_letters

phrase = 'This is an example using Python'
print(phrase)

print(ascii_letters)

# Set theory
letters = set(ascii_letters) - set('aeiou')

lower_case_consonants = list(filter(lambda character: character in letters, phrase))
print(lower_case_consonants)

