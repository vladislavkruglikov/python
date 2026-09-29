def decorator(f):
    print("Print this only once, when the function is decorated.")
    return f


def echo(value_to_return):
    return value_to_return


@decorator
def echo_decorated(value_to_return):
    return value_to_return


assert decorator(echo)(5) == echo_decorated(5) == 5
assert decorator(echo)(5) == echo_decorated(5) == 5

# Only 3 prints of "Print this only once, when the function is decorated." will be issued
