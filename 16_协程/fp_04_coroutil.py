# 预激协程的装饰器

from functools import wraps


def coroutine(func):

    """装饰器：向前执行到第一个 `yield` 表达式，预激 `func`"""
    @wraps(func)
    def primer(*args, **kwargs):  # <1>把被装饰的生成器函数替换成这里的 primer 函数；调用 primer 函数时，返回预激后的生成器。
        gen = func(*args, **kwargs)  # <2>调用被装饰的函数，获取生成器对象。
        next(gen)  # <3>预激生成器。
        return gen  # <4>返回生成器。

    return primer
