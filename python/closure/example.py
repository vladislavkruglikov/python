def make_multiplier(factor):
    def multiply(x):
        return x * factor
    # Returned multiply is closure it retains access to factor from its enclosing function
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

assert double(5) == 10
assert triple(5) == 15

# Closures can be used for decorators or stateful functions
