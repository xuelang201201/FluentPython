from array import array
import reprlib
import math


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

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        # 我们只需在 Vector2d.frombytes 方法的基础上改动最后一行：
        # 直接把 memoryview 传给构造方法，不用像前面那样使用 * 拆包。
        return cls(memv)
