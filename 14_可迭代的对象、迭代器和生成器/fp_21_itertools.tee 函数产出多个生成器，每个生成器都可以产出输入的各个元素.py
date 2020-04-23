import itertools

print(list(itertools.tee('ABC')))
# [<itertools._tee object at 0x7f2c287342c0>, <itertools._tee object at 0x7f2c28734300>]
g1, g2 = itertools.tee('ABC')
print(next(g1))
# A
print(next(g2))
# A
print(next(g2))
# B
print(list(g1))
# ['B', 'C']
print(list(g2))
# ['C']
print(list(zip(*itertools.tee('ABC'))))
# [('A', 'A'), ('B', 'B'), ('C', 'C')]
