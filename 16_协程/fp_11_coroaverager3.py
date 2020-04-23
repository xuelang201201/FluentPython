# 使用 yield from 计算平均值并输出统计报告

from collections import namedtuple

Result = namedtuple('Result', 'count average')


# 子生成器
def averager():  # <1>与 fp_09 中的 averager 协程一样。这里作为子生成器使用。
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield  # <2>main 函数中的客户代码发送的各个值绑定到这里的 term 变量上。
        if term is None:  # <3>至关重要的终止条件。如果不这样做，使用 yield from 调用这个协程的生成器会永远阻塞。
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)  # <4>返回的 Result 会成为 grouper 函数中的 yield from 表达式的值。


# 委派生成器
def grouper(results, key):  # <5>grouper 是委派生成器。
    while True:  # <6>这个循环每次迭代时会新建一个 averager 实例；每个实例都是作为协程使用的生成器对象。
        # <7>grouper 发送的每个值都会经由 yield from 处理，通过管道传给 averager 实例。
        # grouper 会在 yield from 表达式处暂停，等待 averager 实例处理客户端发来的值。
        # averager 实例运行完毕后，返回的值绑定到 results[key] 上。while 循环会不断创建
        # averager 实例，处理更多的值。
        results[key] = yield from averager()


# 客户端代码，即调用方
def main(data):  # <8>main 函数是客户端代码，用 PEP 380 定义的术语来说，是 “调用方”。这是驱动一切的函数。
    results = {}
    for key, values in data.items():
        # <9>group 是调用 grouper 函数得到的生成器对象，传给 grouper 函数的第一个参数是
        # results，用于收集结果；第二个参数是某个键。group 作为协程使用。
        group = grouper(results, key)
        next(group)  # <10>预激 group 协程。
        for value in values:
            # <11>把各个 value 传给 grouper。传入的值最终到达 averager 函数中 term = yield 那一行；
            # grouper 永远不知道传入的值是什么。
            group.send(value)
        # <12>把 None 传入 grouper，导致当前的 averager 实例终止，也让 grouper 继续运行，再创
        # 建一个 averager 实例，处理下一组值。
        group.send(None)  # 重要！

    # print(results)  # 如果要调试，去掉注释
    report(results)


# 输出报告
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit
        ))


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}


if __name__ == '__main__':
    main(data)
