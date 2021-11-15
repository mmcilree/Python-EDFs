# Copied from: https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
# Checks if all items in in iterable are equal
def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)