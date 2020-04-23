# 调用 BingoCage 实例，从打乱的列表中取出一个元素

import random


class BingoCage:

    def __init__(self, items):
        self._items = list(items)  # __init__ 接受任何可迭代对象；在本地构建一个副本，防止列表参数的意外副作用。
        random.shuffle(self._items)  # shuffle 定能完成工作，因为 self._items 是列表。

    def pick(self):  # 起主要作用的方法。
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')  # 如果 self._items 为空，抛出异常，并设定错误消息。

    def __call__(self):  # bingo.pick() 的快捷方式是 bingo()。
        return self.pick()


bingo = BingoCage(range(3))
print(bingo.pick())

print(bingo())

print(callable(bingo))  # 判断对象能否调用
