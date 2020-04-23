"""
======================
AddableBingoCage tests
======================


Tests for __add__:

# BEGIN ADDABLE_BINGO_ADD_DEMO

    >>> vowels = 'AEIOU'
    >>> globe = AddableBingoCage(vowels)  # <1>使用 5 个元素（vowels 中的各个字母）创建一个 globe 实例。
    >>> globe.inspect()
    ('A', 'E', 'I', 'O', 'U')
    >>> globe.pick() in vowels  # <2>从中取出一个元素，确认它在 vowels 中。
    True
    >>> len(globe.inspect())  # <3>确认 globe 的元素数量减少到 4 个了。
    4
    >>> globe2 = AddableBingoCage('XYZ')  # <4>创建第二个实例，它有 3 个元素。
    >>> globe3 = globe + globe2
    >>> len(globe3.inspect())  # <5>把前两个实例加在一起，创建第 3 个实例。这个实例有 7 个元素。
    7
    >>> void = globe + [10, 20]  # <6>AddableBingoCage 实例无法与列表相加，抛出 TypeError。那个错误消息是 __add__ 方法返回 NotImplemented 时 Python 解释器输出的。
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for +: 'AddableBingoCage' and 'list'

# END ADDABLE_BINGO_ADD_DEMO


Tests for __iadd__:

# BEGIN ADDABLE_BINGO_IADD_DEMO

    >>> globe_orig = globe  # <1>复制一份，供后面检查对象的标识。
    >>> len(globe.inspect())  # <2>现在 globe 有 4 个元素。
    4
    >>> globe += globe2  # <3>AddableBingoCage 实例可以从同属一类的其他实例那里接受元素。
    >>> len(globe.inspect())
    7
    >>> globe += ['M', 'N']  # <4>+= 的右操作数也可以是任何可迭代对象。
    >>> len(globe.inspect())
    9
    >>> globe is globe_orig  # <5>在这个示例中，globe 始终指代 globe_orig 对象。
    True
    >>> globe += 1  # <6>AddableBingoCage 实例不能与非可迭代对象相加，错误消息会指明原因。
    Traceback (most recent call last):
      ...
    TypeError: right operand in += must be 'AddableBingoCage' or an iterable

# END ADDABLE_BINGO_IADD_DEMO
"""

# BEGIN ADDABLE_BINGO

# <1>“PEP 8——Style Guide for Python Code” (https://www.python.org/dev/peps/pep-0008/#imports) 建议，
# 把导入标准库的语句放在导入自己编写的模块之前。
import itertools

from tombola import Tombola
from bingo import BingoCage


class AddableBingoCage(BingoCage):  # <2>AddableBingoCage 扩展 BingoCage。

    def __add__(self, other):
        if isinstance(other, Tombola):  # <3>__add__方法的第二个操作数只能是 Tombola 实例。
            # <4>如果 other 是 Tombola 实例，从中获取元素。
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()  # <5>否则，尝试使用 other 创建迭代器。
        else:
            try:
                other_iterable = iter(other)
            # <6>如果尝试失败，抛出异常，并且告知用户该怎么做。如果可能，错误消息应该明确指导用户怎么解决问题。
            except TypeError:
                self_cls = type(self).__name__
                msg = "right operand in += must be {!r} or an iterable"
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)  # <7>如果能执行到这里，把 other_iterable 载入 self。
        return self  # <8>重要提醒：增量赋值特殊方法必须返回 self。

# END ADDABLE_BINGO
