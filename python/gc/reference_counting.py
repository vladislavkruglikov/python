a = [1, 2]
b = a

del a  # Removes the name a, the list is still referenced by b
del b  # Last reference removed, CPython normally deallocates the list
