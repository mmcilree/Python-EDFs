# Get the difference between elements either as numbers or tuples
def difference_mod(el1, el2, mod):
    if type(el1) is tuple and type(el2) is tuple:
        res = ()
        for i in range(0, len(el1)):
            res = res + tuple([(el1[i] - el2[i]) % mod])
        return res
    else:
        return (el1 - el2) % mod

def difference_mult(el1, el2, mult):
    # TODO
    pass  
# Get all the external differences between sets as a dict
def get_ed(sets, modulus):
    results = {}
    for i in range(0, len(sets)):
        for j in range(0, len(sets)):
            if i != j:
                for el1 in sets[i]:
                    for el2 in sets[j]:
                        results[
                            tuple([el1, el2])
                        ] = difference_mod(el1, el2, modulus)
    return results

# Get all the external differences between one set and a set of other sets 
# as a dict
def get_ed_from_set(from_set, to_sets, modulus):
    results = {}
    for i in range(0, len(from_set)):
        for j in range(0, len(to_sets)):
            el1 = from_set[i]
            for el2 in to_sets[j]:
                results[
                    tuple([el1, el2])
                ] = difference_mod(el1, el2, modulus)

    return results

# Print all external differences aligned for latex
def print_ed(sets, modulus, sort=True, perline=6):
    ed = get_ed(sets, modulus)
    if sort:
        ed = dict(sorted(ed.items(), key=lambda item: item[1]))
    count = 0
    for diff in ed.keys():
        print("& " + str(diff[0]) + " - " + str(diff[1]) + " = " + str(ed[diff]))
        count += 1
        if count % perline == 0:
            print("\\\\")

# Print all external differences for a particular set aligned for latex
def print_ed_from_set(sets, i, modulus, sort=True, perline=6):
    ed = get_ed_from_set(sets[i], sets[0:i] + sets[i+1:len(sets)], modulus)
    if sort:
        ed = dict(sorted(ed.items(), key=lambda item: item[1]))
    
    count = 0
    for diff in ed.keys():
        print("& " + str(diff[0]) + " - " + str(diff[1]) + " = " + str(ed[diff]))
        count += 1
        if count % perline == 0:
            print("\\\\")

# Copied from: https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
# Checks if all items in in iterable are equal
def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)


# Check if a given collection of sets is an edf
def is_edf(sets, modulus):

    if not all_equal([len(s) for s in sets]):
        return False

    ed = get_ed(sets, modulus)
    counts = [sum([v == val for v in ed.values()]) for val in range(1, modulus)]
    
    return all_equal(counts)

def is_overlapping_edf(sets, modulus):
    ed = get_ed(sets, modulus)
    counts = [sum([v == val for v in ed.values()]) for val in range(1, modulus) if val != 0]

    return all_equal(counts)

# Check if a given collection of sets is a strong edf
def is_sedf(sets, modulus):
    if not all_equal([len(s) for s in sets]):
        return False

    overall_counts = []
    for i in range(0, len(sets)):
        ed = get_ed_from_set(sets[i], sets[0:i] + sets[i+1:len(sets)], modulus)
        counts = [sum([v == val for v in ed.values()]) for val in range(1, modulus)]
        if not all_equal(counts):
            return False
        overall_counts.append(counts)
    
    return all_equal(overall_counts)

