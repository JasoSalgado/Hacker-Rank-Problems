# Take values from a list less than 100 and then, sum 10 to each oneclear

numbers = [150, 250, 183, 50, 10, 330, 25, 67]
print('Example: ', numbers)

less_than_100 = filter(lambda n: n < 100, numbers)
result = list(map(lambda n: n + 10, less_than_100))
print(result)

numbers2 = [10, 20, 30, 653, 253, 1478, 1256, 1, 9, 8]
print('Example two:', numbers2)

minor_100 = filter(lambda n: n < 100, numbers2)
result2 = list(map(lambda n: n + 10, minor_100))
print(result2)