import itertools


def vowel(c):
    return c.lower() in 'aeiou'


print(list(filter(vowel, 'Aardvark')))
# ['A', 'a', 'a']
print(list(itertools.filterfalse(vowel, 'Aardvark')))
# ['r', 'd', 'v', 'r', 'k']
print(list(itertools.dropwhile(vowel, 'Aardvark')))
# ['r', 'd', 'v', 'a', 'r', 'k']
print(list(itertools.takewhile(vowel, 'Aardvark')))
# ['A', 'a']
print(list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1))))
# ['A', 'r', 'd', 'a']
print(list(itertools.islice('Aardvark', 4)))
# ['A', 'a', 'r', 'd']
print(list(itertools.islice('Aardvark', 4, 7)))
# ['v', 'a', 'r']
print(list(itertools.islice('Aardvark', 1, 7, 2)))
# ['a', 'd', 'a']
