# LotteryBlower 是 Tombola 的具体子类，覆盖了继承的 inspect 和 loaded 方法

import random

from fp_08_tombola import Tombola


class LotteryBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable)  # 初始化方法接受任何可迭代对象：把参数构建成列表。

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            # 如果范围为空，random.randrange(...) 函数抛出 ValueError，为了兼容
            # Tombola，我们捕获它，抛出 LookupError。
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)  # 否则，从 self._balls 中取出随机选中的元素。

    # 覆盖 loaded 方法，避免调用 inspect 方法（fp_09 中的 Tombola.loaded
    # 方法是这么做的）。我们可以直接处理 self._balls 而不必构建整个有序元组，从而提升速度。
    def loaded(self):
        return bool(self._balls)

    def inspect(self):  # 使用一行代码覆盖 inspect 方法。
        return tuple(sorted(self._balls))
