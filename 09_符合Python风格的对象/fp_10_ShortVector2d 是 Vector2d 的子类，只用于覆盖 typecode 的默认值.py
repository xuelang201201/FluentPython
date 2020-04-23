from fp_07_vector2d_v3 import Vector2d


class ShortVector2d(Vector2d):  # 把 ShortVector2d 定义为 Vector2d 的子类，只用于覆盖 typecode 类属性。
    typecode = 'f'


sv = ShortVector2d(1 / 11, 1 / 27)  # 为了演示，创建一个 ShortVector2d 实例，即 sv。
print(sv)
# >>> sv
# ShortedVector2d(0.09090909090909091, 0.037037037037037035)  # 查看 sv 的 repr 表现形式。
print(len(bytes(sv)))  # 确认得到的字节序列长度为 9 字节，而不是之前的 17 字节。
