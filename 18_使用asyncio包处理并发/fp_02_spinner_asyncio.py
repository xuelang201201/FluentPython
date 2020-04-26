"""通过协程以动画形式显示文本式旋转指针"""

import asyncio
import itertools


async def spin(msg):  # <1>打算交给 asyncio 处理的协程需要使用 async。
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            await asyncio.sleep(.1)  # <2>使用 await.sleep(.1) 替代 time.sleep(.1)，这样的休眠不会阻塞事件循环。
        # <3>如果 spin 函数苏醒后抛出 asyncio.CancelledError 异常，其原因是发出了取消请求，因此退出循环。
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))


async def slow_function():  # <4>现在，slow_function 函数是协程，在用休眠假装进行 I/O 操作时，使用 await 继续执行事件循环。
    # 假装等待 I/O 一段时间
    await asyncio.sleep(3)  # <5>await.sleep(3) 表达式把控制权交给主循环，在休眠结束后恢复这个协程。
    return 42


async def supervisor():  # <6>现在，supervisor 函数也是协程，因此可以使用 async 驱动 slow_function 函数。
    # <7>asyncio.create_task(...)函数排定 spin 协程的运行时间，使用一个 Task 对象包装 spin 协程，并立即返回。
    spinner = asyncio.create_task(spin('thinking!'))
    # <8>显示Task对象。输出类似于<Task pending coro=<spin() running at spinner_asyncio.py:12>>
    print('spinner object:', spinner)
    # <9>驱动 slow_function() 函数。结束后，获取返回值。同时，事件循环继续运行，因为
    # slow_function 函数最后使用 await asyncio.sleep(3) 表达式把控制权交回给了主循环。
    result = await slow_function()
    # <10>Task对象可以取消；取消后会在协程当前暂停处抛出 asyncio.CancelledError 异常。
    # 协程可以捕获这个异常，也可以延迟取消，甚至拒绝取消。
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()  # <11>获取事件循环的引用。
    # <12>驱动 supervisor 协程，让它运行完毕；这个协程的返回值是这次调用的返回值。
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
