from fp_04_diamond import D

d = D()
d.pingpong()

# 第一个调用是 self.ping()，运行的是 D 类的 ping 方法，输出这一行和下一行。
# ping: <fp_04_diamond.D object at 0x7fe920c2a760>
# post-ping: <fp_04_diamond.D object at 0x7fe920c2a760>
# 第二个调用是 super().ping()，跳过 D 类的 ping 方法，找到 A 类的 ping 方法。
# ping: <fp_04_diamond.D object at 0x7fe920c2a760>
# 第三个调用是 self.pong()，根据 __mro__，找到的是 B 类实现的 pong 方法。
# pong: <fp_04_diamond.D object at 0x7fe920c2a760>
# 第四个调用 super().pong(), 也根据 __mro__，找到 B 类实现的 pong 方法。
# pong: <fp_04_diamond.D object at 0x7fe920c2a760>
# 第五个调用的是 C.pong(self)，忽略 __mro__，找到的是 C 类实现的 pong 方法。
# PONG: <fp_04_diamond.D object at 0x7fe920c2a760>
