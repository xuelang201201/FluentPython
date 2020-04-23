def simple_coroutine():  # <1>协程使用生成器函数定义：定义体中有 yield 关键字。
    print('-> coroutine started')
    # <2>yield 在表达式中使用；如果协程只需从客户那里接收数据，那么产出的值是 None————
    # 这个值是隐式指定的，因为 yield 关键字右边没有表达式。
    x = yield
    print('-> coroutine received:', x)


my_coro = simple_coroutine()
print(my_coro)  # <3>与创建生成器的方式一样，调用函数得到生成器对象。
# <generator object simple_coroutine at 0x7fb8327895f0>

# <4>首先要调用 next(...) 函数，因为生成器还没启动，
# 没在 yield 语句处暂停，所以一开始无法发送数据。
print(next(my_coro))
# -> coroutine started

# <5>调用这个方法后，协程定义体中的 yield 表达式会计算出 42；
# 现在，协程会恢复，一直运行到下一个 yield 表达式，或者终止。
print(my_coro.send(42))
# -> coroutine received: 42
# Traceback (most recent call last):  # <6>这里，控制权流动到协程定义体的末尾，导致生成器像往常一样抛出 StopIteration 异常。
#   ...
# StopIteration
