"""
    >>> coro_avg = averager()  # <1>创建协程对象。
    >>> next(coro_avg)  # <2>调用 next 函数，预激协程。
    >>> coro_avg.send(10)  # <3>计算移动平均值：多次调用 .send(...) 方法，产出当前的平均值。
    10.0
    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0
"""


# 定义一个计算移动平均值的协程
def averager():
    total = 0.0
    count = 0
    average = None
    # <1>这个无限循环表明，只要调用方不断把值发给这个协程，它就会一直接收值，然后生成
    # 结果。仅当调用方在协程上调用 .close() 方法，或者没有对协程的引用而被垃圾回收程
    # 序回收时，这个协程才会终止。
    while True:
        # <2>这里的 yield 表达式用于暂停执行协程，把结果发给调用方；还用于接收调用方
        # 后面发给协程的值，恢复无线循环。
        term = yield average
        total += term
        count += 1
        average = total / count
