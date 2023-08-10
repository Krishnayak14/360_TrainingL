# Write a Person class with an instance variable “age” and a constructor that takes an integer as a
# parameter. The constructor must assign the integer value to the age variable after confirming the
# argument passed is not negative; if a negative argument is passed then the constructor should set
# age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
# methods:
# yearPasses() should increase age by the integer value that you are passing inside the function.
# amIOld() should perform the following conditional actions:I
# f age is between 0 and <13, print “You are young”.
# If age is >=13 and <=19 , print “You are a teenager”.
# Otherwise, print “You are old”.

class Person:
    def __init__(self, age):
        if age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0")
        else:
            self.age = age

    def yearPasses(self, years):
        if years >= 0:
            self.age += years
        else:
            print("Invalid input for years. Age remains unchanged.")

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age <= 19:
            print("You are a teenager.")
        else:
            print("You are old.")

# Example usage
person = Person(-1)
person.amIOld()

person.yearPasses(4)
person.amIOld()

person.yearPasses(10)
person.amIOld()

person = Person(16)
person.amIOld()

person.yearPasses(18)
person.amIOld()

person.yearPasses(64)
person.amIOld()

person.yearPasses(38)
person.amIOld()

