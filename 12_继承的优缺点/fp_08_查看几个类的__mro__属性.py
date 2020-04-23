import numbers
# <5>io 模块中有抽象基类（名称以 ...Base 后缀结尾）和具体类，如 BytesIO 和 TextIOWrapper。
#    open() 函数返回的对象属于这些类型，具体要根据模型参数而定。
import io  # <5>
from frenchdeck2 import FrenchDeck2

print(bool.__mro__)  # <1>bool 从 int 和 object 中继承方法和属性。


def print_mro(cls):  # <2>print_mro 函数使用更紧凑的方式显示方法和解析顺序。
    print(', '.join(c.__name__ for c in cls.__mro__))


print_mro(bool)
# bool, int, object
print_mro(FrenchDeck2)  # <3>FrenchDeck2 类的祖先包含 collections.abc 模块中的几个抽象基类。
# FrenchDeck2, MutableSequence, Sequence, Reversible, Collection, Sized, Iterable, Container, object
print_mro(numbers.Integral)  # <4>这些是 numbers 模块提供的几个数字抽象基类。
# Integral, Rational, Real, Complex, Number, object
print_mro(io.BytesIO)
# BytesIO, _BufferedIOBase, _IOBase, object
print_mro(io.TextIOWrapper)
# TextIOWrapper, _TextIOBase, _IOBase, object
