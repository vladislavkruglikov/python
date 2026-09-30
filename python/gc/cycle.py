a = []
a.append(a)
del a
# The list still has a reference from itself—but your program 
# can no longer reach it. Reference counting alone cannot reclaim it. 
# The cyclic collector can detect and collect it.
