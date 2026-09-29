def decorator(value_to_return):
    print("Print this only once, when the function is decorated.")
    def _f(f):
        print("Print this only once too, when the function is decorated.")
        def __f(*args, **kwargs):
            print("Print this on each function call")
            args = list(args)
            args[0] = value_to_return
            return f(*args, **kwargs)
        return __f
    return _f


def echo(value_to_return):
    return value_to_return


@decorator(value_to_return=52)
def echo_decorated(value_to_return):
    return value_to_return


assert decorator(52)(echo)(52) == echo_decorated(52) == 52
assert decorator(52)(echo)(52) == echo_decorated(52) == 52

# Only 3 prints of "Print this only once, when the function is decorated." will be issued
# Only 3 prints of "Print this only once too, when the function is decorated." will be issued
# And 4 times "Print this on each function call"
