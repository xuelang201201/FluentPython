import os

lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates  # 元组拆包
print(latitude)
print(longitude)

# 可以用 * 运算符把一个可迭代对象拆开作为函数的参数
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
quotient, remainder = divmod(*t)
print((quotient, remainder))

# 让一个函数可以用元组的形式返回多个值
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)

# 用*来处理剩下的元素
a, b, *rest = range(5)
print((a, b, rest))
a, b, *rest = range(3)
print((a, b, rest))
a, b, *rest = range(2)
print((a, b, rest))

a, *body, c, d = range(5)
print((a, body, c, d))
*head, b, c, d = range(5)
print((head, b, c, d))
