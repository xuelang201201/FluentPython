"""
A two-dimensional vector class

    >>> v1 = Vector2d(3, 4)
    >>> print(v1.x, v1.y)
    3.0 4.0
    >>> x, y = v1
    >>> x, y
    (3.0, 4.0)
    >>> v1
    >>> Vector2d(3.0, 4.0)
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
    >>> bool(v1), bool(Vector2d(0, 0))
    (True, False)

Test of ''.frombytes()'' class method:

    >>> v1_clone = Vector2d.frombytes(bytes(v1))
    >>> v1_clone
    Vector2d(3.0, 4.0)
    >>> v1 == v1_clone
    True

Test of ''format()'' with Cartesian coordinates:

    >>> format(v1)
    '(3.0, 4.0)'
    >>> format(v1, '.2f')
    '(3.00, 4.00)'
    >>> format(v1, '.3e')
    '(3.000e+00, 4.000e+00)'

Test of the ''angle'' method::

    >>> Vector2d(0, 0).angle()
    0.0
    >>> Vector2d(1, 0).angle()
    0.0
    >>> epsilon = 10**-8
    >>> abs(Vector2d(0, 1).angle() - math.pi/2) < epsilon
    True
    >>> abs(Vector2d(1, 1).angle() - math.pi/4) < epsilon
    True

Test of ''format()'' with polar coordinates:

    >>> format(Vector2d(1, 1), 'p')
    '<1.4142135623730951, 0.7853981633974483>'
    >>> format(Vector2d(1, 1), '.3ep')
    '<1.414e+00, 7.854e-01>'
    >>> format(Vector2d(1, 1), '0.5fp')
    '<1.41421, 0.78540>'

Test of 'x' and 'y' read-only properties:

    >>> v1.x, v1.y
    (3.0, 4.0)
    >>> v1.x = 123
    Traceback (most recent call last):
      ...
    AttributeError: can't set attribute

Test of hashing:

    >>> v1 = Vector2d(3, 4)
    >>> v2 = Vector2d(3.1, 4.2)
    >>> hash(v1), hash(v2)
    (7, 384307168202284039)
    >>> len(set([v1, v2]))
    2

"""

from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)  # 使用两个前导下划线（尾部没有下划线，或者有一个下划线），把属性标记为私有的。
        self.__y = float(y)

    @property  # @property 装饰器把读值方法标记为特性。
    def x(self):  # 读值方法与公开属性同名，都是 x。
        return self.__x  # 直接返回 self.__x。

    @property  # 以同样的方式处理 y 特性。
    def y(self):
        return self.__y

    def __iter__(self):
        # 需要读取 x 和 y 分量的方法可以保持不变，通过 self.x 和 self.y 读取公开特性，而不必读取私有属性，
        # 因此上述代码清单省略了这个类的其他代码。
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        # __repr__ 方法使用 {!r} 获取各个分量的表示形式，然后插值，构成一个字符串；
        # 因为 Vector2d 实例是可迭代的对象，所以 *self 会把 x 和 y 分量提供给 format 函数。
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))  # 从可迭代的 Vector2d 实例中可以轻松地得到一个元组，显示为一个有序对。

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +  # 为了生成字节序列，我们把 typecode 转换成字节序列，然后……
                bytes(array(self.typecode, self)))  # ……迭代 Vector2d 实例，得到一个数组，再把数组转换成字节序列。

    def __eq__(self, other):
        # 为了快速比较所有分量，在操作数中构建元组。对 Vector2d 实例来说，可以这样做，不过仍有问题。
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)  # 模是 x 和 y 分量构成的直角三角形的斜边长。

    def __bool__(self):
        # __bool__ 方法使用 abs(self) 计算模，然后把结果转换成布尔值，因此，0.0 是 False，非零值是 True。
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)  # 使用 math.atan2() 函数计算角度。

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):  # 如果格式代码以 'p' 结尾，使用极坐标。
            fmt_spec = fmt_spec[:-1]  # 从 fmt_spec 中删除 'p' 后缀。
            coords = (abs(self), self.angle())  # 构建一个元组，表示极坐标：(magnitude, angle)。
            outer_fmt = '<{}, {}>'  # 把外层格式设为一对尖括号。
        else:
            coords = self  # 如果不以 'p' 结尾，使用 self 的 x 和 y 分量构建直角坐标。
            outer_fmt = '({}, {})'  # 把外层格式设为一对圆括号。
        # 使用内置的 format 函数把 fmt_spec 应用到向量的各个分量上，构建一个可迭代的格式化字符串。
        components = (format(c, fmt_spec) for c in coords)  # 使用各个分量生成可迭代的对象，构成格式化字符串。
        return outer_fmt.format(*components)  # 把格式化字符串代入外层格式。

    @classmethod  # 类方法使用 classmethod 装饰器修饰。
    def frombytes(cls, octets):  # 不用传入 self 参数；相反，要通过 cls 传入类本身。
        typecode = chr(octets[0])  # 从第一个字节中读取 typecode。
        # 使用传入的 octets 字节序列创建一个 memoryview，然后使用 typecode 转换。
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)  # 拆包转换后的 memoryview，得到构造方法所需的一对参数。

