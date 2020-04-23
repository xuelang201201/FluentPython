print(slice)  # slice 是内置的类型。
# <class 'slice'>
print(dir(slice))  # 通过审查 slice，发现它有 start、stop 和 step 数据属性，以及 indices 方法。
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
# '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', 'indices', 'start', 'step', 'stop']

"""
S.indices(len) -> (start, stop, stride)
    给定长度为 len 的序列，计算 S 表示的扩展切片的起始（start）和结尾（stop）索引，
    以及步幅（stride）。超出边界的索引会被截掉，这与常规切片的处理方式一样。
"""

# 假设长度为 5 的序列，例如 'ABCDE'。
print(slice(None, 10, 2).indices(5))  # 'ABCDE'[:10:2] 等同于 'ABCDE'[0:5:2]
# (0, 5, 2)
print(slice(-3, None, None).indices(5))  # 'ABCDE'[-3:] 等同于 'ABCDE'[2:5:1]
# (2, 5, 1)
