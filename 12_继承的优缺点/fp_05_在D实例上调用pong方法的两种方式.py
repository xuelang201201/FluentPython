from fp_04_diamond import *

d = D()
d.pong()  # 直接调用 d.pong() 运行的是 B 类中的版本。
C.pong(d)  # 超类中的方法都可以直接调用，此时要把实例作为显式参数传入。
# 方法解析顺序 __mro__
print(D.__mro__)
# (<class 'fp_04_diamond.D'>, <class 'fp_04_diamond.B'>, <class 'fp_04_diamond.C'>,
# <class 'fp_04_diamond.A'>, <class 'object'>)
