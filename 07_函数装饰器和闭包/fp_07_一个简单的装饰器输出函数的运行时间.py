import time


def clock(func):
    def clocked(*args):  # 定义内部函数 clocked，它接受任意个定位参数。
        t0 = time.perf_counter()
        result = func(*args)  # 这行代码可用，是因为 clocked 的闭包中包含自由变量 func。
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked  # 返回内部函数，取代被装饰的函数。
