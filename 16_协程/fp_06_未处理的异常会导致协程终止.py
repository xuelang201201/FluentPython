from fp_05_coroaverager1 import averager

coro_avg = averager()
print(coro_avg.send(40))  # <1>使用 @coroutine 装饰器装饰的 averager 协程，可以立即开始发送值。
# 40.0
print(coro_avg.send(50))
# 45.0
print(coro_avg.send('spam'))  # <2>发送的值不是数字，导致协程内部有异常抛出。
# Traceback (most recent call last):
# ...
# TypeError: unsupported operand type(s) for +=: 'float' and 'str'
print(coro_avg.send(60))  # <3>由于在协程内没有处理异常，协程会终止。如果试图重新激活协程，会抛出 StopIteration 异常。
# Traceback (most recent call last):
#   FIle "<stdin>", line 1, in <module>
# StopIteration
