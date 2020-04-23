def f(m, n):
    m += n
    return m


x = 1
y = 2
print(f(x, y))
print((x, y))  # 数字 x 没变。
a = [1, 2]
b = [3, 4]
print(f(a, b))
print((a, b))  # 列表 a 变了。
t = (10, 20)
u = (30, 40)
print(f(t, u))
print((t, u))  # 元组 t 没变。
