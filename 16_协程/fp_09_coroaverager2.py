# 定义一个求平均值的协程，让它返回一个结果
"""
说明 averager 行为的 doctest

    >>> coro_avg = averager()
    >>> next(coro_avg)
    >>> coro_avg.send(10)  # <1>这一版不产出值。
    >>> coro_avg.send(30)
    >>> coro_avg.send(6.5)

    # <2>发送 None 会终止循环，导致协程结束，返回结果。一如既往，生成器对象会
    # 抛出 StopIteration 异常。异常对象的 value 属性保存着返回的值。
    >>> coro_avg.send(None)
    Traceback (most recent call last):
      ...
    StopIteration: Result(count=3, average=15.5)


捕获 StopIteration 异常，获取 averager 返回的值

    >>> coro_avg = averager()
    >>> next(coro_avg)
    >>> coro_avg.send(10)
    >>> coro_avg.send(30)
    >>> coro_avg.send(6.5)
    >>> try:
    ...     coro_avg.send(None)
    ... except StopIteration as exc:
    ...     result = exc.value
    ...
    >>> result
    Result(count=3, average=15.5)

"""

from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break  # <1>为了返回值，协程必须正常终止；因此，这一版 averager 中有个条件判断，以便退出累计循环。
        total += term
        count += 1
        average = total / count
    # <2>返回一个 namedtuple，包含 count 和 average 两个字段。在 Python 3.3 之前，如果生成器返回值，解释器会报句法错误。
    return Result(count, average)
