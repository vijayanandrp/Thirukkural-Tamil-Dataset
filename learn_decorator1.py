def outer(func):
    def inner():
        print("Accessing: ", func.__name__)
        return func()

    return inner


@outer
def greet():
    print("Hello!!")


# x = outer(greet)
# x()

# greet = outer(greet)
greet()
