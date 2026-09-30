x = 10


def change():
    x = 20  # Local to change()


change()
assert x == 10
