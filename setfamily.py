from utils import all_equal


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
                if i != j :
                    ext_diffs = self.external_differences(i, j)

                    counts = [
                        sum([v == val for v in ext_diffs.values()])
                        for val in range(1, self.n)
                    ]

                    all_counts.append(counts)

        return all_equal(all_counts)


if __name__ == "__main__":
    mod_5_mult = [
        [0, 1, 2, 3, 4],
        [1, 2, 3, 4, 0],
        [2, 3, 4, 0, 1],
        [3, 4, 0, 1, 2],
        [4, 0, 1, 2, 3],
    ]

    test = SetFamily([[0, 1], [2, 4]], mod_5_mult)
    print(test.mult(2, 3))
    print(test.diff(4, 1))
    print(test.diff(2, 3))
    print(test.is_edf())  # True
    print(test.is_sedf()) # True
