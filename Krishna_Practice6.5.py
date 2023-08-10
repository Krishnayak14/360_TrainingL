#6.5
def message_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

#@message_decorator
def greet():
    print("Hello, world!")

greet()
