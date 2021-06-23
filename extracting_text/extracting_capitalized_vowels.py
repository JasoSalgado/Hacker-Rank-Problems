# Extract capitalize vowels from a text using the function filter

phrase = 'This is just An Example'
print(phrase)

capitalize_vowels = list(filter(lambda character: character in 'AEIOU', phrase))


print(capitalize_vowels)