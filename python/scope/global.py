x = 10


def change():
    global x
    x = 20


change()
assert x == 20
