def echo(value_to_return):
    return value_to_return


def decorator(f):
    print("Print this only once, when the function is decorated.")
    return f


def decorator_2(f):
    print("Second decorator.")
    return f


@decorator_2
@decorator
def echo_decorated(value_to_return):
    return value_to_return


assert decorator_2(decorator(echo)(5)) == echo_decorated(5) == 5
