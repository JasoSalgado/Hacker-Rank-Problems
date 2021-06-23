"""
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
Function Description

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

int number: the maximum value to print
Prints

The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.

Input Format

A single integer denoting .
"""
def print_formatted(number):
    l1 = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        print(str(i).rjust(l1,' '), end=" ")
        print(oct(i)[2:].rjust(l1, ' '), end=" ")
        print(((hex(i)[2:]).upper()).rjust(l1,' '),end=" ")
        print(bin(i)[2:].rjust(l1, ' '), end=" ")
        print("")