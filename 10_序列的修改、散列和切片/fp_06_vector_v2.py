"""
>>> v7 = Vector(range(7))
>>> v7[-1]  # 单个整数索引只获取一个分量，值为浮点数。
6.0
>>> v7[1:4]  # 切片索引创建一个新 Vector 实例。
Vector([1.0, 2.0, 3.0])
>>> v7[-1:]  # 长度为 1 的切片也创建一个 Vector 实例。
Vector([6.0])
>>> v7[1, 2]  # Vector 不支持多维索引，因此索引元组或多个切片会抛出错误。
Traceback (most recent call last)
  ...
TypeError: Vector indices must be integers
"""

from array import array
import reprlib
import math
import numbers


class Vector:
    typecode = 'd'

    def __init__(self, components):
        # self._components 是 “受保护的” 实例属性，把 Vector 的分量保存在一个数组中。
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)  # 为了迭代，我们使用 self._components 构建一个迭代器。

    def __repr__(self):
        # 使用 reprlib.repr() 函数获取 self._components 的有限长度表示
        # 形式（如 array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])）。
        components = reprlib.repr(self._components)
        # 把字符串插入 Vector 的构造方法调用之前，去掉前面的 array('d' 和后面的)。
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))  # 直接使用 self._components 构建 bytes 对象。

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        # 不能使用 hypot 方法了，因此我们先计算各分量的平方之和，然后再使用 sqrt 方法开平方。
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    # 能处理切片的 __getitem__ 方法
    def __getitem__(self, index):
        cls = type(self)  # 获取实例所属的类（即 Vector），供后面使用。
        if isinstance(index, slice):  # 如果 index 参数的值是 slice 对象……
            return cls(self._components[index])  # ……调用类的构造方法，使用 _components 数组的切片构建一个新 Vector 实例。
        elif isinstance(index, numbers.Integral):  # 如果 index 是 int 或其他整数类型……
            return self._components[index]  # ……那就返回 _components 中相应的元素。
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))  # 否则，抛出异常。

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        # 我们只需在 Vector2d.frombytes 方法的基础上改动最后一行：
        # 直接把 memoryview 传给构造方法，不用像前面那样使用 * 拆包。
        return cls(memv)
