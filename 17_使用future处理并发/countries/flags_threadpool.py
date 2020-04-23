"""使用 futures.ThreadPoolExecutor 类实现多线程下载的脚本"""

from concurrent import futures

from flags import save_flag, get_flag, show, main  # <1>重用 flags 模块中的几个函数。

MAX_WORKERS = 20  # <2>设定 ThreadPoolExecutor 类最多使用几个线程。


def download_one(cc):  # <3>下载一个图像的函数；这是在各个线程中执行的函数。
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    # <4> 设定工作的线程数量：使用允许的最大值（MAX_WORKERS）与要处理的数量之间较小的
    # 那个值，以免创建多余的线程。
    workers = min(MAX_WORKERS, len(cc_list))
    # <5>使用工作的线程数实例化 ThreadPoolExecutor 类；executor.__exit__ 方法会调用
    # executor.shutdown(wait=True) 方法，它会在所有线程都执行完毕前阻塞线程。
    with futures.ThreadPoolExecutor(workers) as executor:
        # <6>map 方法的作用与内置的 map 函数类似，不过 download_one 函数会在多个线程中并发调用；
        # map 方法返回一个生成器，因此可以迭代，获取各个函数返回的值。
        res = executor.map(download_one, sorted(cc_list))

    # <7>返回获取的结果数量；如果有线程抛出异常，异常会在这里抛出，
    # 这与隐式调用 next() 函数从迭代器中获取相应的返回值一样。
    return len(list(res))


if __name__ == '__main__':
    main(download_many)  # <8>调用 flags 模块中的 main 函数，传入 download_many 函数的增强版。
