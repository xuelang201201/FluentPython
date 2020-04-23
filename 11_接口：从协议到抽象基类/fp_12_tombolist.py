"""
# 注册之后，可以使用 issubclass 和 isinstance 函数判断 TomboList 是不是 Tombola 的子类：
>>> from fp_08_tombola import Tombola
>>> from fp_12_tombolist import TomboList
>>> issubclass(TomboList, Tombola)
True
>>> t = TomboList(range(100))
>>> isinstance(t, Tombola)
True
"""

# TomboList 是 Tombola 的虚拟子类

from random import randrange

from fp_08_tombola import Tombola


@Tombola.register  # 把 Tombolist 注册为 Tombola 的虚拟子类。
class TomboList(list):  # Tombolist 扩展 list。

    def pick(self):
        if self:  # TomboList 从 list 中继承了 __bool__ 方法，列表不为空时返回 True。
            position = randrange(len(self))
            return self.pop(position)  # pick 调用继承自 list 的 self.pop 方法，传入一个随机的元素索引。
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend  # Tombolist.load 与 list.extend 一样。

    def loaded(self):
        return bool(self)  # loaded 方法委托 bool 函数。

    def inspect(self):
        return tuple(sorted(self))

# Tombola.register(TomboList)  # 如果是 Python 3.3 或之前的版本，不能把 .register 当作类装饰器使用，必须使用标准的调用句法。
