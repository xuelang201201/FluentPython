# 定义Tombola抽象基类的子类
# BingoCage 是 Tombola 的具体子类

import random

from fp_08_tombola import Tombola


class BingoCage(Tombola):  # 明确指定 BingoCage 类扩展 Tombola 类。

    def __init__(self, items):
        # 假设我们将在线上游戏中使用这个。random.SystemRandom 使用 os.urandom(...) 函数实现 random API。
        # 根据 os 模块的文档（http://docs.python.org/3/library/os.html#os.urandom），os.urandom(...)
        # 函数生成 “适合用于加密” 的随机字节序列。
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)  # 委托 .load(...) 方法实现初始加载。

    def load(self, items):
        self._items.extend(items)
        # 没有使用 random.shuffle() 函数，而是使用 SystemRandom 实例的 .shuffle() 方法。
        self._randomizer.shuffle(self._items)

    def pick(self):  # pick 方法的实现方式与 fp_08 中的一样。
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):  # __call__ 也跟 fp_08 中的一样。它没必要满足 Tombola 接口，添加额外的方法没有问题。
        self.pick()
