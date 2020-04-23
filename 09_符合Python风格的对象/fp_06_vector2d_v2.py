"""
In [1]: from fp_06_vector2d_v2 import Vector2d                                                                                                                           

In [2]: format(Vector2d(1, 1), 'p')                                                                                                                                      
Out[2]: '<1.4142135623730951, 0.7853981633974483>'

In [3]: format(Vector2d(1, 1), '.3ep')                                                                                                                                   
Out[3]: '<1.414e+00, 7.854e-01>'

In [4]: format(Vector2d(1, 1), '0.5fp')                                                                                                                                  
Out[4]: '<1.41421, 0.78540>'

"""
from array import array
import math


class Vector2d:
    typecode = 'd'  # typecode 是类属性，在 Vector2d 实例和字节序列之间转换时使用。

    def __init__(self, x, y):
        # 在 __init__ 方法中把 x 和 y 转换成浮点数，尽早捕获错误，以防调用 Vector2d 函数时传入不当参数。
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        # 定义 __iter__ 方法，把 Vector2d 实例变成可迭代的对象，这样才能拆包（例如，x, y = my_vector）。
        # 这个方法的实现方式很简单，直接调用生成器表达式一个接一个产出分量。
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

    def __abs__(self):
        return math.hypot(self.x, self.y)  # 模是 x 和 y 分量构成的直角三角形的斜边长。

    def __bool__(self):
        # __bool__ 方法使用 abs(self) 计算模，然后把结果转换成布尔值，因此，0.0 是 False，非零值是 True。
        return bool(abs(self))

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

    def angle(self):
        return math.atan2(self.y, self.x)  # 使用 math.atan2() 函数计算角度。

    @classmethod  # 类方法使用 classmethod 装饰器修饰。
    def frombytes(cls, octets):  # 不用传入 self 参数；相反，要通过 cls 传入类本身。
        typecode = chr(octets[0])  # 从第一个字节中读取 typecode。
        # 使用传入的 octets 字节序列创建一个 memoryview，然后使用 typecode 转换。
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)  # 拆包转换后的 memoryview，得到构造方法所需的一对参数。
