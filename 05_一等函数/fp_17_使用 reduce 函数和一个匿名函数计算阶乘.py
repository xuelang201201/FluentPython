# 支持函数式编程的包 ———— operator 模块

from functools import reduce


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))
