# 使用示例 fp_04 中定义的 @coroutine 装饰器定义并测试计算移动平均值的协程
"""
用于计算移动平均值的协程

# <1>调用 averager() 函数创建一个生成器对象，在 coroutine 装饰器的 primer 函数中已经预激了这个生成器。
    >>> coro_avg = averager()
    >>> from inspect import getgeneratorstate

# <2>getgeneratorstate 函数指明，处于 GEN_SUSPENDED 状态，因此这个协程已经准备好，可以接收值了。
    >>> getgeneratorstate(coro_avg)
    'GEN_SUSPENDED'

# <3>可以立即开始把值发给 coro_avg————这正是 coroutine 装饰器的目的。
    >>> coro_avg.send(10)
    10.0
    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0
"""

from fp_04_coroutil import coroutine  # <4>导入 coroutine 装饰器。


@coroutine  # <5>把装饰器应用到 averager 函数上。
def averager():  # <6>函数的定义体与 fp_03 完全一样。
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count
