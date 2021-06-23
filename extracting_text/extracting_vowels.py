# Extract lower case vowels from a text using the function filter

phrase = 'This Is A Real Example Of Extracting Vowels'
print(phrase)

lower_case_vowels = list(filter(lambda character: True if character in 'aeiou' else False, phrase))

print(lower_case_vowels)