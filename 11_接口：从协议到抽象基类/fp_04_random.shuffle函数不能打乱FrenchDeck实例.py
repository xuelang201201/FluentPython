from random import shuffle
from fp_02_实现序列协议的FrenchDeck类 import FrenchDeck

deck = FrenchDeck()
shuffle(deck)
# Traceback (most recent call last):
#   File "<stdin>", line 5, in <module>
#     shuffle(deck)
#   File "/usr/lib/python3.8/random.py", line 307, in shuffle
#     x[i], x[j] = x[j], x[i]
# TypeError: 'FrenchDeck' object does not support item assignment
