from random import shuffle
from fp_02_实现序列协议的FrenchDeck类 import FrenchDeck

deck = FrenchDeck()


def set_card(deck, position, card):  # 定义一个函数，它的参数为 deck、position 和 card。
    deck._cards[position] = card


FrenchDeck.__setitem__ = set_card  # 把那个函数赋值给 FrenchDeck 类的 __setitem__ 属性。
shuffle(deck)  # 现在可以打乱 deck 了，因为 FrenchDeck 实现了可变序列协议所需的方法。
print(deck[:5])
