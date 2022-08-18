def count_bits(n):
    a = bin(n)
    return a[2:].count("1")


q = 'AAAABBBCCDAABBB'
a = q.index("B", 2)
r = "B"
print(q.index("A", 1) - q.index(r, a+4))


def unique_in_order(iterable):
    items = []
    for a in iterable:
        i = iterable.index(a)
        if iterable.index(a) - iterable.index(a, i + 1) < 2:
            if iterable[i] == iterable[i + 1]:
                items.append(iterable[i])

    return items
