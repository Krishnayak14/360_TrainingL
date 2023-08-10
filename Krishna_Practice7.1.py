#1. Write a program that calculates and prints the value according to the given formula:
#Q= Square root of [(2*C*D)/H]

import math

C = 50
H = 30
numbers = input("Enter value of D: ")
numbers = numbers.split(',')

result = []
for D in numbers:
    Q = round(math.sqrt(2 * C * int(D) / H))
    result.append(Q)

print(result)
