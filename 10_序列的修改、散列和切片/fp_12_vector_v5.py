"""
A multidimensional ''Vector'' class, take 5

A ''Vector'' is built from an iterable of numbers::

    >>> Vector([3.1, 4.2])
    Vector([3.1, 4.2])
    >>> Vector((3, 4, 5))
    Vector([3.0, 4.0, 5.0])
    >>> Vector(range(10))
    Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])


Tests with two dimensions (same results as ''vector2d_v1.py'')::

    >>> v1 = Vector([3, 4])
    >>> x, y = v1
    >>> x, y
    (3.0, 4.0)
    >>> v1
    Vector([3.0, 4.0])
    >>> v1_clone = eval(repr(v1))
    >>> v1 == v1_clone
    True
    >>> print(v1)
    (3.0, 4.0)
    >>> octets = bytes(v1)
    >>> octets
    b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'
    >>> abs(v1)
    5.0
    >>> bool(v1), bool(Vector([0, 0]))
    (True, False)


Test of ''.frombytes()'' class method:

    >>> v1_clone = Vector.frombytes(bytes(v1))
    >>> v1_clone
    Vector([3.0, 4.0])
    >>> v1 == v1_clone
    True


Tests with three dimensions::

    >>> v1 = Vector([3, 4, 5])
    >>> x, y, z = v1
    >>> x, y, z
    (3.0, 4.0, 5.0)
    >>> v1
    Vector([3.0, 4.0, 5.0])
    >>> v1_clone = eval(repr(v1))
    >>> v1 == v1_clone
    True
    >>> print(v1)
    (3.0, 4.0, 5.0)
    >>> abs(v1)
    7.0710678118654755
    >>> bool(v1), bool(Vector([0, 0, 0]))
    (True, False)


Tests with many dimensions::

    >>> v7 = Vector(range(7))
    >>> v7
    Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
    >>> abs(v7)
    9.539392014169456


Test of ''.__bytes__'' and ''.frombytes()'' methods::

    >>> v1 = Vector([3, 4, 5])
    >>> v1_clone = Vector.frombytes(bytes(v1))
    >>> v1_clone
    Vector([3.0, 4.0, 5.0])
    >>> v1 == v1_clone
    True


Tests of sequence behavior::

    >>> v1 = Vector([3, 4, 5])
    >>> len(v1)
    3
    >>> v1[0], v1[len(v1)-1], v1[-1]
    (3.0, 5.0, 5.0)


Test of slicing::

    >>> v7 = Vector(range(7))
    >>> v7[-1]
    6.0
    >>> v7[1:4]
    Vector([1.0, 2.0, 3.0])
    >>> v7[-1:]
    Vector([6.0])
    >>> v7[1,2]
    Traceback (most recent call last):
      ...
    TypeError: Vector indices must be integers


Tests of dynamic attribute access::

    >>> v7 = Vector(range(10))
    >>> v7.x
    0.0
    >>> v7.y, v7.z, v7.t
    (1.0, 2.0, 3.0)


Dynamic attribute lookup failures::

    >>> v7.k
    Traceback (most recent call last):
      ...
    AttributeError: 'Vector' object has no attribute 'k'
    >>> v3 = Vector(range(3))
    >>> v3.t
    Traceback (most recent call last):
      ...
    AttributeError: 'Vector' object has no attribute 't'
    >>> v3.spam
    Traceback (most recent call last):
      ...
    AttributeError: 'Vector' object has no attribute 'spam'


Tests of hashing::

    >>> v1 = Vector([3, 4])
    >>> v2 = Vector([3.1, 4.2])
    >>> v3 = Vector([3, 4, 5])
    >>> v6 = Vector(range(6))
    >>> hash(v1), hash(v3), hash(v6)
    (7, 2, 1)


Most hash values of non-integers vary from a 32-bit to 64-bit CPython build::

    >>> import sys
    >>> hash(v2) == (384307168202284039 if sys.maxsize > 2**32 else 357915986)
    True


Tests of ``format()`` with Cartesian coordinates in 2D::

    >>> v1 = Vector([3, 4])
    >>> format(v1)
    '(3.0, 4.0)'
    >>> format(v1, '.2f')
    '(3.00, 4.00)'
    >>> format(v1, '.3e')
    '(3.000e+00, 4.000e+00)'


Tests of ``format()`` with Cartesian coordinates in 3D and 7D::

    >>> v3 = Vector([3, 4, 5])
    >>> format(v3)
    '(3.0, 4.0, 5.0)'
    >>> format(Vector(range(7)))
    '(0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)'


Tests of ``format()`` with spherical coordinates in 2D, 3D and 4D::

    >>> format(Vector([1, 1]), 'h')  # doctest:+ELLIPSIS
    '<1.414213..., 0.785398...>'
    >>> format(Vector([1, 1]), '.3eh')
    '<1.414e+00, 7.854e-01>'
    >>> format(Vector([1, 1]), '0.5fh')
    '<1.41421, 0.78540>'
    >>> format(Vector([1, 1, 1]), 'h')  # doctest:+ELLIPSIS
    '<1.73205..., 0.95531..., 0.78539...>'
    >>> format(Vector([2, 2, 2]), '.3eh')
    '<3.464e+00, 9.553e-01, 7.854e-01>'
    >>> format(Vector([0, 0, 0]), '0.5fh')
    '<0.00000, 0.00000, 0.00000>'
    >>> format(Vector([-1, -1, -1, -1]), 'h')  # doctest:+ELLIPSIS
    '<2.0, 2.09439..., 2.18627..., 3.92699...>'
    >>> format(Vector([2, 2, 2, 2]), '.3eh')
    '<4.000e+00, 1.047e+00, 9.553e-01, 7.854e-01>'
    >>> format(Vector([0, 1, 0, 0]), '0.5fh')
    '<1.00000, 1.57080, 0.00000, 0.00000>'
"""

# Vector 类最终版的 doctest 和全部代码；带标号的那几行是为了支持 __format__ 方法而添加的代码。

from array import array
import reprlib
import math
import numbers
import functools  # 为了使用 reduce 函数，导入 functools 模块。
import operator  # 为了使用 xor 函数，导入 operator 模块。
import itertools  # <1> 为了在 __format__ 方法中使用 chain 函数，导入 itertools 模块。


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
        # if len(self) != len(other):  # 如果两个对象的长度不一样，那么它们不相等。
        #     return False
        # # zip 函数生成一个由元组构成的生成器，元组中的元素来自参数传入的各个可迭代对象。
        # # 前面比较长度的测试是必要的，因为一旦有一个输入耗尽，zip 函数会立即停止生长值，而且不发出警告。
        # for a, b in zip(self, other):
        #     if a != b:  # 只要有两个分量不同，返回 False，退出。
        #         return False
        # return True  # 否则，对象是相等的。

        # 以上代码等同于
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        # hashes = (hash(x) for x in self._components)  #
        # 创建一个生成器表达式，惰性计算各个分量的散列值。
        hashes = map(hash, self._components)
        # 把 hashes 提供给 reduce 函数，使用 xor 函数计算聚合的散列值；第三个参数，0 是初始值。
        return functools.reduce(operator.xor, hashes, 0)

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

    def angle(self, n):  # <2>使用 “n 维球体” 词条（http://en.wikipedia.org/wiki/N-sphere）中的公式计算莫个角坐标。
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):  # <3> 创建生成器表达式，按需计算所有角坐标。
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):  # 超球面坐标
            fmt_spec = fmt_spec[:-1]
            # <4> 使用 itertools.chain 函数生成生成器表达式，无缝迭代向量的模和各个角坐标。
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'  # <5> 配置使用尖括号显示球面坐标。
        else:
            coords = self
            outer_fmt = '({})'  # <6> 配置使用圆括号显示笛卡儿坐标。
        components = (format(c, fmt_spec) for c in coords)  # <7> 创建生成器表达式，按需格式化各个坐标元素。
        return outer_fmt.format(', '.join(components))  # <8> 把以括号分隔的格式化分量插入尖括号或圆括号。

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        # 我们只需在 Vector2d.frombytes 方法的基础上改动最后一行：
        # 直接把 memoryview 传给构造方法，不用像前面那样使用 * 拆包。
        return cls(memv)
