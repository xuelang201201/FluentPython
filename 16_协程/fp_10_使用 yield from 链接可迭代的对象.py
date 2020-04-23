def chain(*iterables):
    for it in iterables:
        yield from it


s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t)))
# ['A', 'B', 'C', 0, 1, 2]
