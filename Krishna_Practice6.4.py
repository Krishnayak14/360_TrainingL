#6.4


input_string = "Consultadd Training"

reversed_generator = (char for char in reversed(input_string))

reversed_string = ''.join(reversed_generator)

print("Reversed String:", reversed_string)
