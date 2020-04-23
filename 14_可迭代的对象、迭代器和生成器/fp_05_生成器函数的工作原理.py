def gen_123():  # 只要 Python 函数中包含关键字 yield，该函数就是生成器函数。
    yield 1  # 生成器函数的定义中通常都有循环，不过这不是必要条件；这里重复使用 3 次 yield。
    yield 2
    yield 3


print(gen_123)
# <function gen_123 at 0x7f53b60a1dc0>  # 仔细看，gen_123 是函数对象。
print(gen_123())
# <generator object gen_123 at 0x7f53b60a8660>  # 但是调用时，gen_123() 返回一个生成器对象。

for i in gen_123():  # 生成器是迭代器，会生成传给 yield 关键字的表达式的值。
    print(i)
# 1
# 2
# 3

g = gen_123()  # 为了仔细检查，我们把生成器对象赋值给 g。
next(g)  # 因为 g 是迭代器，所以调用 next(g) 会获取 yield 生成的下一个元素。
# 1
next(g)
# 2
next(g)
# 3
next(g)  # 生成器函数的定义体执行完毕后，生成器对象会抛出 StopIteration 异常。
# Traceback (most recent call last):
#   ...
# StopIteration
