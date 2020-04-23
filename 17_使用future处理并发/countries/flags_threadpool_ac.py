# 把 download_many 函数中的 executor.map 方法换成 executor.submit 方法和 futures.as_completed 函数

from concurrent import futures

from flags import save_flag, get_flag, show, main


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    cc_list = cc_list[:5]  # <1>这次演示只使用人口最多的 5 个国家。
    # <2>把 max_workers 硬编码为3，以便在输出中观察待完成的 future。
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):  # <3>按照字母表顺序迭代国家代码，明确表明输出的顺序与输入一致。
            # <4>executor.submit 方法排定可调用对象的执行时间，然后返回一个 future，表示这个待执行的操作。
            future = executor.submit(download_one, cc)
            to_do.append(future)  # <5>存储各个 future，后面传给 as_completed 函数。
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))  # <6>显示一个消息，包含国家代码和对应的 future。

        results = []
        for future in futures.as_completed(to_do):  # <7>as_completed 函数在 future 运行结束后产出 future。
            res = future.result()  # <8>获取该 future 的结果。
            msg = '{} results: {!r}'
            print(msg.format(future, res))  # <9>显示 future 及其结果。
            results.append(res)

    return len(results)


if __name__ == '__main__':
    main(download_many)

"""flags_threadpool_ac.py 脚本的输出"""
# <1>排定的 future 按字母表排序；future 的 repr() 方法会显示 future 的状态：前三个 future
# 的状态是 running，因为有三个工作的线程。
# Scheduled for BR: <Future at 0x7f89a1514fd0 state=running>
# Scheduled for CN: <Future at 0x7f89a1530730 state=running>
# Scheduled for ID: <Future at 0x7f89a1530a00 state=running>
# Scheduled for IN: <Future at 0x7f89a0cbe2e0 state=pending>  # <2>后两个 future 的状态是 pending，等待有线程可用。
# Scheduled for US: <Future at 0x7f89a0cbec70 state=pending>
# <3>这一行里的第一个 CN 是运行在一个工作线程中的 download_one 函数输出的，随后的内容是 download_many 函数输出的。
# CN <Future at 0x7f89a1530730 state=finished returned str> results: 'CN'
# <4>这里有两个线程输出国家代码，然后主线程中的 download_many 函数输出第一个线程的结果。
# BR ID <Future at 0x7f89a1530a00 state=finished returned str> results: 'BR'
# <Future at 0x7f89a1514fd0 state=finished returned str> results: 'ID'
# US <Future at 0x7f89a0cbec70 state=finished returned str> results: 'US'
# IN <Future at 0x7f89a0cbe2e0 state=finished returned str> results: 'IN'
