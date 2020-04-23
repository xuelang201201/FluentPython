t1 = (1, 2, 3)
t2 = tuple(t1)  # t1 和 t2 绑定到同一个对象。
print(t2 is t1)
t3 = t1[:]
print(t3 is t1)  # t3 也是。
