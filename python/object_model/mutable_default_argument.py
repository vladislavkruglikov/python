def add_item(item, items=[]):
    items.append(item)
    return items

assert add_item("a") == ["a"]
assert add_item("b") == ["a", "b"]


# Better option 
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


assert add_item("a") == ["a"]
assert add_item("b") == ["b"]
