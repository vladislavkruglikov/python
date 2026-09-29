def add_item(item, items=[]):
    items.append(item)
    return items

assert add_item("a") == ["a"]
assert add_item("b") == ["a", "b"]
