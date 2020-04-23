# 学习在协程中处理异常的测试代码
"""
激活和关闭 demo_exc_handling，没有异常

    >>> exc_coro = demo_exc_handling()
    >>> next(exc_coro)
    -> coroutine started
    >>> exc_coro.send(11)
    -> coroutine received: 11
    >>> exc_coro.send(22)
    -> coroutine received: 22
    >>> exc_coro.close()
    >>> from inspect import getgeneratorstate
    >>> getgeneratorstate(exc_coro)
    'GEN_CLOSED'


把 DemoException 异常传入 demo_exc_handling 不会导致协程中止

    >>> exc_coro = demo_exc_handling()
    >>> next(exc_coro)
    -> coroutine started
    >>> exc_coro.send(11)
    -> coroutine received: 11
    >>> exc_coro.throw(DemoException)
    *** DemoException handled. Continuing...
    >>> getgeneratorstate(exc_coro)
    'GEN_SUSPENDED'


如果无法处理传入的异常，协程会终止

    >>> exc_coro = demo_exc_handling()
    >>> next(exc_coro)
    -> coroutine started
    >>> exc_coro.send(11)
    -> coroutine received: 11
    >>> exc_coro.throw(ZeroDivisionError)
    Traceback (most recent call last):
      ...
    ZeroDivisionError
    >>> getgeneratorstate(exc_coro)
    'GEN_CLOSED'

"""


class DemoException(Exception):
    """为这次演示定义的异常类型。"""


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:  # <1>特别处理 DemoException 异常。
            print('*** DemoException handled. Continuing...')
        else:  # <2>如果没有异常，那么显示接收到的值。
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')  # <3>这一行永远不会执行。
