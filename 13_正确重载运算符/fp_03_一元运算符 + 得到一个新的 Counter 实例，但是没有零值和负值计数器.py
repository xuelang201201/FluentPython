from collections import Counter

ct = Counter('abracadabra')
print(ct)
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct['r'] = -3
ct['d'] = 0
print(ct)
# Counter({'a': 5, 'b': 2, 'c': 1, 'd': 0, 'r': -3})
print(+ct)
# Counter({'a': 5, 'b': 2, 'c': 1})
