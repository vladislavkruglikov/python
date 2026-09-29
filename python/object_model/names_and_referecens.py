# In CPython a list is a resizable array of references to objects
a = [1, 2]

# This binds the name b to the same list object. It creates no 
# new list, and b does not point to a.
b = a

# Evaluate the right-hand side: obtain the object representing 5.
# Make a refer to that object, releasing its previous reference to 2.
# If the old object’s reference count reaches zero, ordinary CPython 
# reference counting can deallocate it directly.
b[0] = 5

# ----------------

A = [[1], [2], [3]]
B = A * 2

assert B == [[1], [2], [3], [1], [2], [3]]

# B[0] and B[3] refer to the same inner list, also referenced by A[0].
# Replace that list's element at index 0 with a reference to the integer 9.
B[0][0] = 9

assert B == [[9], [2], [3], [9], [2], [3]]
