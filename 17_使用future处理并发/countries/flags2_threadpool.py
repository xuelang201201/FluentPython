import collections
from concurrent import futures

import requests
import tqdm  # <1>导入显示进度条的库

from flags2_common import main, HTTPStatus  # <2>从 flags2_common 模块中导入一个函数和一个 Enum。
from flags2_sequential import download_one  # <3>重用 flags2_sequential 模块里的 download_one 函数。

# <4>如果没有在命令行中指定 -m/--max_req 选项，使用这个值作为并发请求数的最大值，也就是线程池的大小；
# 真是的数量可能会比这少，例如下载的国旗数量较少。
DEFAULT_CONCUR_REQ = 30
# <5>不管要下载多少国旗，也不管 -m/--max_req 命令行选项的值是多少，MAX_CONCUR_REQ 会
# 限制最大的并发请求数；这是一项安全预防措施。
MAX_CONCUR_REQ = 1000


def download_many(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    # <6>把 max_workers 设为 concur_req，创建 ThreadPoolExecutor 实例；main 函数会把下面这
    # 三个值中最小的那个赋值给 concur_req：MAX_CONCUR_REQ、cc_list 的长度、-m/--max_req 命令
    # 行选项的值。这样能避免创建超过所需的线程。
    with futures.ThreadPoolExecutor(max_workers=concur_req) as executor:
        to_do_map = {}  # <7>这个字典把各个 Future 实例（表示一次下载）映射到相应的国家代码上，在处理错误时使用。
        # <8>按字母顺序迭代国家代码列表。结果的顺序主要由 HTTP 响应的时间长短决定，不过，
        # 如果线程池的大小（由 concur_req 设定）比 len(cc_list)小得多，可能会发现有按
        # 字母顺序批量下载的情况。
        for cc in sorted(cc_list):
            # <9>每次调用 executor.submit 方法排定一个可调用对象的执行时间，然后返回一个 Future 实例。
            # 第一个参数是可调用的对象，其余的参数是传给可调用对象的参数。
            future = executor.submit(download_one, cc, base_url, verbose)
            to_do_map[future] = cc  # <10>把返回的 future 和国家代码存储在字典中。
        # <11>futures.as_completed 函数返回一个迭代器，在 future 运行结束后产出 future。
        done_iter = futures.as_completed(to_do_map)
        if not verbose:
            # <12>如果不是详细模式，把 as_completed 函数返回的结果传给 tqdm 函数，显示进度条；因为
            # done_iter 没有 len 函数，所以我们必须通过 total= 参数告诉 tqdm 函数预期的元素数量，
            # 这样 tqdm 才能预计剩余的工作量。
            done_iter = tqdm.tqdm(done_iter, total=len(cc_list))
        for future in done_iter:  # <13>迭代运行结束后的 future。
            try:
                # <14>在 future 上调用 result 方法，要么返回可调用对象的返回值，要么抛出可调用的对象
                # 在执行过程中捕获的异常。这个方法可能会阻塞，等待确定结果；不过，在这个示例中不会阻塞，
                # 因为 as_completed 函数只返回已经运行结束的 future。
                res = future.result()
            # <15>处理可能出现的异常；这个函数余下的代码与依序下载版 download_many 函数一
            # 样（见 flags2_sequential.py），不过下一点除外。
            except requests.exceptions.HTTPError as exc:
                error_msg = 'HTTP {res.status_code} - {res.reason}'
                error_msg = error_msg.format(res=exc.response)
            except requests.exceptions.ConnectionError as exc:
                error_msg = 'Connection error'
            else:
                error_msg = ''
                status = res.status

            if error_msg:
                status = HTTPStatus.error
            counter[status] += 1
            if verbose and error_msg:
                # <16>为了给错误消息提供上下文，以当前的 future 为键，从 to_do_map 中获取国家代码。在
                # 依序下载版中无须这么做，因为那一版迭代的是国家代码，所以知道当前国家的代码；而这里迭
                # 代的是 future。
                cc = to_do_map[future]
                print('*** Error for {}: {}'.format(cc, error_msg))
    return counter


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
