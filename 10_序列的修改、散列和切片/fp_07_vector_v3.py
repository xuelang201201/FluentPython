"""
# 不恰当的行为：为 v.x 赋值没有抛出错误，但是前后矛盾
# 之所以前后矛盾，是 __getattr__ 的运作方式导致的：仅当对象没有指定名称的属性时，Python 才会调用那个方法，
# 这是一种后备机制。可是，像 v.x = 10 这样赋值之后，v 对象有 x 属性了，因此使用了 v.x 获取 x 属性的值时
# 不会调用 __getattr__ 方法了，解释器直接返回绑定到 v.x 上的值，即 10。另一方面，__getattr__ 方法的实现
# 没有考虑 self._components 之外的实例属性，而是从这个属性中获取 shortcut_names 中所列的 “虚拟属性”。

>>> v = Vector(range(5))
>>> v
Vector([0.0, 1.0, 2.0, 3.0, 4.0])
>>> v.x  # 使用 v.x 获取第一个元素（v[0]）。
0.0
>>> v.x = 10  # 为 v.x 赋新值。这个操作应该抛出异常。
>>> v.x  # 读取 v.x，得到的是新值，10。
10
>>> v  # 可是，向量的分量没变。
Vector([0.0, 1.0, 2.0, 3.0, 4.0])
"""

# 在 vector_v2.py 中定的 Vector 类里添加 __getattr__ 方法
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
        # 把字符串插入 Vector 的构造方法调用之前，去掉前面的 array('d' 和后面的 )。
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
            # ……调用类的构造方法，使用 _components 数组的切片构建一个新 Vector 实例。
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):  # 如果 index 是 int 或其他整数类型……
            return self._components[index]  # ……那就返回 _components 中相应的元素。
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))  # 否则，抛出异常。

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)  # 获取 Vector，后面待用。

        if len(name) == 1:  # 如果属性名只有一个字母，可能是 shortcut_names 中的一个。
            # 查找那个字母的位置；str.find 还会定位 'yz'，但是我们不需要，因此在前一行做了测试。
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):  # 如果位置落在范围内，返回数组中对应的元素。
                return self._components[pos]

        # 如果测试都失败了，抛出 AttributeError，并指明标准的消息文本。
        msg = '{.__name__!r} objects has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        # 我们只需在 Vector2d.frombytes 方法的基础上改动最后一行：
        # 直接把 memoryview 传给构造方法，不用像前面那样使用 * 拆包。
        return cls(memv)
