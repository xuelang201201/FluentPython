"""
>>> v = Vector(range(5))
>>> v
Vector([0.0, 1.0, 2.0, 3.0, 4.0])
>>> v.x
0.0
>>> v.x = 10
Traceback (most recent call last)
  ...
AttributeError: readonly attribute 'x'
>>> v.x
0.0
>>> v
Vector([0.0, 1.0, 2.0, 3.0, 4.0])
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

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:  # 特别处理名称是单个字符的属性。
            if name in cls.shortcut_names:  # 如果 name 是 xyzt 中的一个，设置特殊的错误消息。
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():  # 如果 name 是小写字母，为所有小写字母设置一个错误消息。
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''  # 否则，把错误消息设为空字符串。
            if error:  # 如果有错误消息，抛出 AttributeError。
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)

        super(Vector, self).__setattr__(name, value)  # 默认情况：在超类上调用__setattr__方法，提供标准行为。

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        # 我们只需在 Vector2d.frombytes 方法的基础上改动最后一行：
        # 直接把 memoryview 传给构造方法，不用像前面那样使用 * 拆包。
        return cls(memv)
