def numbers():
    print("start")
    yield 10
    print("continue")
    yield 20
    print("finish")


# Nothing printed
g = numbers()

# Prints start
assert next(g) == 10

# Prints continue
assert next(g) == 20

# Prints finish
try:
    next(g)
except StopIteration:
    ...
