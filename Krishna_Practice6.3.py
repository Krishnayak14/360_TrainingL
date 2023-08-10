#6.3 Learn about yield, next and Generators
def reverse_string(string):
    length = len(string)
    for i in range(length - 1, -1, -1):
        yield string[i]
