from fp_01_vector2d_v0 import Vector2d

v1 = Vector2d(3, 4)
print(v1.x, v1.y)  # Vector2d 实例的分量可以直接通过属性访问（无需调用读值方法）。
x, y = v1  # Vector2d 实例可以拆包成变量元组。
print(x, y)
print(v1)  # repr 函数调用 Vector2d 实例，得到的结果类似于构建实例的源码。
v1_clone = eval(repr(v1))  # 这里使用 eval 函数，表明 repr 函数调用 Vector2d 实例得到的是对构造方法的准确表述。
print(v1 == v1_clone)  # Vector2d 实例支持使用 == 比较；这样便于测试。
print(v1)  # print 函数会调用 str 函数，对 Vector2d 来说，输出的是一个有序对。
octets = bytes(v1)  # bytes 函数会调用 __bytes__ 方法，生成实例的二进制表示形式。
print(octets)
print(abs(v1))  # abs 函数会调用 __abs__ 方法，返回 Vector2d 实例的模。
# bool 函数会调用 __bool__ 方法，如果 Vector2d 实例的模为零，返回 False，否则返回 True。
print(bool(v1), bool(Vector2d(0, 0)))
