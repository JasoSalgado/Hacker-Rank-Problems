def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    data = [alphabet[i] for i in range(size)]
    items = list(range(size))
    items = items[:-1] + items[::-1]
    
    for i in items:
        aux = data[-(i + 1):]
        row = aux[::-1] + aux[1:]
        print('-'.join(row).center(size * 4 - 3, '-'))

print_rangoli(5)