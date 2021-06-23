# sort a list of numbers from the modulus calculated for each number.

numbers = [101, 203, 105, 100, 53]
print(numbers)

# Ascending order
ordered_numbers = sorted(numbers, key=lambda n: n % 5)
print(ordered_numbers)

# Descending order 
ordered_numbers = sorted(numbers, key=lambda n: n % 5, reverse = True)
print(ordered_numbers)