a = [7, [1, 2]]

# When I make a shallow copy of a list, Python creates a new list containing 
# references to the same objects as the original list, without duplicating those objects.
b = a.copy()

# Python does not copy the objects
assert id(a[0]) == id(b[0])

# But since a[0] is immutable changing the value will create new object and update refereces in the a
# but does not change references in b. That means if we would copy list but never write to it we would save
# a lot of memory because readings would happen from same referenced memory. But on write we would creat new object
a[0] = 9
assert id(a[0]) != id(b[0])
assert a[0] != b[0]

# Same for mutable list
assert id(a[1]) == id(b[1])
a[1][0] = 9

# We did not change the list itself
assert id(a[1]) == id(b[1])

# So both have references to the same list
assert a[1][0] == b[1][0]

# In contract deep copy recreates immutable objects but for mutable it just copies 
# them since it is safe.
import copy

a = [7, [1, 2]]
b = copy.deepcopy(a)
assert id(a[0]) == id(b[0])
assert id(a[1]) != id(b[1])
