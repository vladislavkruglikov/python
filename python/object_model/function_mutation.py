def mutate(x):
    x.append(3)

a = [1, 2]
mutate(a)

# Python passes an object reference by value
assert a == [1, 2, 3]

# In contrast passing by value creates a separate copy of that object
