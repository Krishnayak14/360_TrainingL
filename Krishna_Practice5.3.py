#3.
user_input= int(input("Please enter a number"))
def validate(num):
    if len(str(num)) > 4:
        print("The number is too long")
    if len(str(num)) < 4:
        print("The number is too short")
validate(user_input)
