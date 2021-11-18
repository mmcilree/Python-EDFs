from utils import all_equal
import itertools


class SetFamily:
    def __init__(self, sets, group_table, inverses=None):
        self.n = len(group_table)
        self.sets = sets
        self.m = len(sets)
        self.group_table = group_table
        self.inverses = inverses or self.get_inverses()

    def get_inverses(self):
        """Create a table of inverses for each element"""
        return [self.group_table[i].index(0) for i in range(self.n)]

    def mult(self, x, y):
        """Find the product of two elements, according to the group table."""
        return self.group_table[x][y]

    def inv(self, x):
        """Find the inverse of an element, according to the group table."""
        return self.inverses[x]

    def diff(self, x, y):
        """
        Get the difference (xy^-1) between two elements, according to the
        group multiplication.
        """
        return self.group_table[x][self.inv(y)]

    def external_differences(self, i, j):
        """Get all the external diferences between the ith and jth sets."""
        ed_dict = {}
        for el1 in self.sets[i]:
            for el2 in self.sets[j]:
                ed_dict[tuple([el1, el2])] = self.diff(el1, el2)
        return ed_dict

    def is_edf(self):
        """Check if this set family is an External Difference Family"""
        if not all_equal([len(s) for s in self.sets]):
            return False

        all_ext_diffs = {}
        for i in range(self.m):
            for j in range(self.m):
                if i != j:
                    all_ext_diffs.update(self.external_differences(i, j))

        counts = [
            sum([v == val for v in all_ext_diffs.values()])
            for val in range(1, self.n)
        ]

        return all_equal(counts)

    def is_sedf(self):
        """Check if this set family is a Strong External Difference Family"""
        if not all_equal([len(s) for s in self.sets]):
            return False

        all_counts = []
        for i in range(self.m):
            for j in range(self.m):
                if i != j:
                    ext_diffs = self.external_differences(i, j)

                    counts = [
                        sum([v == val for v in ext_diffs.values()])
                        for val in range(1, self.n)
                    ]

                    all_counts.append(counts)

        return all_equal(all_counts)

    def el_as_str(self, el):
        """String representation of element: may be overridden in subclasses."""
        return str(el)

    def print_external_differences(
        self, sort_by=None, headings=None, latex=True, perline=5
    ):
        """Pretty print all external differences."""
        ed = {}
        for i in range(self.m):
            for j in range(self.m):
                if i != j:
                    ed.update(self.external_differences(i, j))

        if sort_by == "value":
            ed = dict(sorted(ed.items(), key=lambda item: item[1]))

        count = 0
        for diff in ed.keys():

            print(
                ("& " if latex else " ")
                + self.el_as_str(diff[0])
                + " - "
                + self.el_as_str(diff[1])
                + " = "
                + self.el_as_str(ed[diff]),
                end=" ",
            )
            count += 1
            if count % perline == 0:
                print("\\\\" if latex else "")
        print()


class CyclicSetFamily(SetFamily):
    """Represent a family of sets with elements from the cyclic group Z_n"""
    def __init__(self, sets, mod):
        group_table = [[(i + j) % mod for i in range(mod)] for j in range(mod)]
        inverses = [(-i) % mod for i in range(mod)]
        super(CyclicSetFamily, self).__init__(
            sets, group_table, inverses=inverses
        )


class CyclicProductSetFamily(SetFamily):
    """
        Represent a family of sets with elements from a direct product of cyclic
        groups Z_a1 x Z_a2 x ... Z_ak
    """
    def __init__(self, sets, mod):
        """Expect sets of tuples for initialisation."""
        if type(mod) is not list:
            # If a single integer is given as mod, assume all groups in the 
            # product have that size. 
            mod = [mod for _ in range(len(sets[0][0]))]

        groups = [range(m) for m in mod]
        elements = list(itertools.product(*groups))
        sets = [list(map(elements.index, s)) for s in sets]

        group_table = [
            [
                elements.index(
                    tuple(
                        [
                            (elements[i][k] + elements[j][k]) % mod[k]
                            for k in range(len(mod))
                        ]
                    )
                )
                for i in range(len(elements))
            ]
            for j in range(len(elements))
        ]

        inverses = [
            elements.index(tuple([-elements[i][k] % mod[k] for k in range(len(mod))]))
            for i in range(len(elements))
        ]

        super(CyclicProductSetFamily, self).__init__(
            sets, group_table, inverses=inverses
        )

    def el_as_str(self, el):
        return str(self.elements[el])


if __name__ == "__main__":
    mod_5_mult = [
        [0, 1, 2, 3, 4],
        [1, 2, 3, 4, 0],
        [2, 3, 4, 0, 1],
        [3, 4, 0, 1, 2],
        [4, 0, 1, 2, 3],
    ]

    test = CyclicSetFamily([[0, 1], [2, 4]], 5)
    print(test.mult(2, 3))
    print(test.diff(4, 1))
    print(test.diff(2, 3))
    print(test.is_edf())  # True
    print(test.is_sedf())  # True
    test.print_external_differences(sort_by="value")

    test2 = CyclicProductSetFamily(
        [
            [(1, 2), (2, 1), (2, 2), (2, 3), (3, 2)],
            [(0, 1), (0, 3), (1, 3), (2, 0), (3, 1)],
            [(0, 2), (1, 0), (1, 1), (3, 0), (3, 3)],
        ],
        4,
    )
    print(test2.is_edf())  # True
    print(test2.is_sedf())  # False
