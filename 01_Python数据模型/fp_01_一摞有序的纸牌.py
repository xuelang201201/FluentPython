import collections
from random import choice

# namedtuple用以构造只有少数属性但是没有方法的对象
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # ranks = []
    # for n in range(2, 11):
    #     ranks.append(str(n))
    # ranks = ranks + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        # for suit in self.suits:
        #     for rank in self.ranks:
        #         self._cards = Card(rank, suit)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))

# __getitem__ 方法把[]操作交给了 self._cards 列表
print(deck[0])
print(deck[-1])

# 随机选取一张牌 random.choice
print(choice(deck))

# 查看一摞牌最上面3张
print(deck[:3])
# 只看牌面是A的牌：先抽出索引是12的那张牌，然后向后数13张牌拿一张
print(deck[12::13])

# 仅仅实现了 __getitem()__ 方法，这一摞牌就变成可迭代的了
for card in deck:
    print(card)

# 反向迭代也可以
for card in reversed(deck):
    print(card)

# 如果一个集合类型没有实现 __contains__ 方法，in运算符就会按顺序做一次迭代搜索
# in运算符可以用在FrenchDeck类上，因为它是可迭代的
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)

# 2最小、A最大
# 黑桃最大、红桃次之、方块再次、梅花最小
# 梅花 2 的大小是 0，黑桃 A 是 51
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
