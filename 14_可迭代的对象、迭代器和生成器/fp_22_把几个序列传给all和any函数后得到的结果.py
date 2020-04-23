print(all([1, 2, 3]))
# True
print(all([1, 0, 3]))
# False
print(all([]))
# True
print(any([1, 2, 3]))
# True
print(any([1, 0, 3]))
# True
print(any([0, 0.0]))
# False
print(any([]))
# False
g = (n for n in [0, 0.0, 7, 8])
print(any(g))
# True
print(next(g))
# 8
