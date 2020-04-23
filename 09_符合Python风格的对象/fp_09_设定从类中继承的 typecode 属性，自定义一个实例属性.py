from fp_07_vector2d_v3 import Vector2d

v1 = Vector2d(1.1, 2.2)
dumpd = bytes(v1)
print(dumpd)
print(len(dumpd))  # 默认的字节序列长度为 17 个字节。
v1.typecode = 'f'  # 把 v1 实例的 typecode 属性设为 'f'。
dumpf = bytes(v1)
print(dumpf)
print(len(dumpf))  # 现在得到的字节序列是 9 个字节长。
print(Vector2d.typecode)  # Vector2d.typecode 属性的值不变，只有 v1 实例的 typecode 属性使用 'f'。
