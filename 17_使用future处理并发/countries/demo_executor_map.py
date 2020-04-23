"""简单演示 ThreadPoolExecutor 类的 map 方法"""

from concurrent import futures
from time import sleep, strftime


def display(*args):  # <1>这个函数的作用很简单，把传入的参数打印出来，并在前面加上 [HH:MM:SS] 格式的时间戳。
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


# <2>loiter 函数什么也没做，只是在开始时显示一个消息，然后休眠 n 秒，
# 最后在结束时再显示一个消息；消息使用制表符缩进，缩进的量由 n 的值确定。
def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t' * n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t' * n, n))
    return n * 10  # <3>loiter 函数返回 n * 10，以便我们了解收集结果的方式。


def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3)  # <4>创建 ThreadPoolExecutor 实例，有 3 个线程。
    # <5>把五个任务提交给 executor（因为只有 3 个线程，所以只有 3 个任务会立即开始：
    # loiter(0)、loiter(1) 和 loiter(2)）；这是非阻塞调用。
    results = executor.map(loiter, range(5))
    display('results:', results)  # <6>立即显示调用 executor.map 方法的结果：一个生成器，如下所示。
    display('Waiting for individual results:')
    # <7>for 循环中的 enumerate 函数会隐式调用 next(results)，这个函数又会在（内部）表示
    # 第一个任务（loiter(0)）的 _f future 上调用 _f.future() 方法。result 方法会阻塞，
    # 直到 future 运行结束，因此这个循环每次迭代时都要等待下一个结果做好准备。
    for i, result in enumerate(results):
        display('result {}: {}'.format(i, result))


main()

"""
 ~/Python/Code/FluentPython/17_使用future处理并发/ python3 demo_executor_map.py 
[16:37:15] Script starting.  # <1>
[16:37:15] loiter(0): doing nothing for 0s...  # <2>
[16:37:15] loiter(0): done.
[16:37:15] 	loiter(1): doing nothing for 1s...  # <3>
[16:37:15] 		loiter(2): doing nothing for 2s...
[16:37:15] results: <generator object Executor.map.<locals>.result_iterator at 0x7f0216b986d0>  # <4>
[16:37:15] 			loiter(3): doing nothing for 3s...  # <5>
[16:37:15] Waiting for individual results:
[16:37:15] result 0: 0  # <6>
[16:37:16] 	loiter(1): done.  # <7>
[16:37:16] 				loiter(4): doing nothing for 4s...
[16:37:16] result 1: 10  # <8>
[16:37:17] 		loiter(2): done.  # <9>
[16:37:17] result 2: 20
[16:37:18] 			loiter(3): done.
[16:37:18] result 3: 30
[16:37:20] 				loiter(4): done.  # <10>
[16:37:20] result 4: 40
"""

"""
<1> 这次运行从 16:37:15 开始。
<2> 第一个线程执行 loiter(0)，因此休眠 0 秒，甚至会在第二个线程开始之前就结束，不过具体情况因人而异。
<3> loiter(1) 和 loiter(2) 立即开始（因为线程池中有三个职程，可以并发运行三个函数）。
<4> 这一行表明，executor.map 方法返回的结果（results）是生成器；不管有多少任务，也不管 max_workers 的值是多少，目前不会阻塞。
<5> loiter(0) 运行结束了，第一个职程可以启动第四个线程，运行 loiter(3)。
<6> 此时执行过程可能阻塞，具体情况取决于传给 loiter 函数的参数：results 生成器的 __next__ 方法必须等到第一个 future 运行结束。
    此时不会阻塞，因为 loiter(0) 在循环开始前结束。注意，这一点之前的所有事件都在同一刻发生————16:37:15。
<7> 一秒钟后，即 16:37:16，loiter(1) 运行完毕。这个线程闲置，可以开始运行 loiter(4)。
<8> 显示 loiter(1) 的结果：10。现在，for 循环会阻塞，等待 loiter(2) 的结果。
<9> 同上：loiter(2) 运行结束，显示结果；loiter(3) 也一样。
<10> 2 秒钟后 loiter(4) 运行结束，因为 loiter(4) 在 16:37:16 时开始，休眠了 4 秒。
"""
