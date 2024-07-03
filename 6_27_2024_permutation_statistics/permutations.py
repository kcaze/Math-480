import itertools


def length(perm):
    n = len(perm)
    return sum([perm[i] > perm[j] for i, j in itertools.combinations(range(n), 2)])


def parity(perm):
    return length(perm) % 2


def descent_set(perm):
    return [i for i in range(len(perm) - 1) if perm[i] > perm[i + 1]]


def num_descents(perm):
    return len(descent_set(perm))


def is_grassmannian(perm):
    return int(num_descents(perm) <= 1)


def is_pattern_avoiding(perm, pattern):
    k = len(pattern)
    for idxs in itertools.combinations(range(len(perm)), k):
        subperm = [perm[i] for i in idxs]
        sorted_subperm = sorted(subperm)
        if all([sorted_subperm[pattern[i] - 1] == subperm[i] for i in range(k)]):
            return 0
    return 1


def has_no_fixed_points(perm):
    return all([perm[i] != i + 1 for i in range(len(perm))])


def ends_in_one(perm):
    return perm[-1] == 1


def descent_at_end(perm):
    return perm[-2] > perm[-1]


def is_involution(perm):
    return all(perm[perm[i] - 1] == i + 1 for i in range(len(perm)))
