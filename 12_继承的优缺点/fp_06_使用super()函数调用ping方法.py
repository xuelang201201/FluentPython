from fp_04_diamond import D

d = D()
d.ping()  # D 类的 ping 方法做了两次调用。

# 第一个调用是 super().ping()；super 函数把 ping 调用委托给 A 类；这一行由 A.ping 输出。
# ping: <fp_04_diamond.D object at 0x7f1dc01ebe80>

# 第二个调用是 print('post-ping:', self)，输出的是这一行。
# post-ping: <fp_04_diamond.D object at 0x7f1dc01ebe80>
