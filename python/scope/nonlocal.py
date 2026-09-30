count = 0


def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = make_counter()

assert counter() == 1
assert counter() == 2
assert count == 0
