"""
全部使用默认值运行 flags2_sequential.py 脚本：LOCAL 服务器，人口最多的 20 国国旗，1 个并发连接::

    $ python3 flags2_sequential.py
    LOCAL site: http://localhost:8001/flags
    Searching for 20 flags: from BD to VN
    1 concurrent connection will be used.
    100%|██████████████████████████████| 20/20 [00:00<00:00, 716.75it/s]
    --------------------
    20 flags downloaded.
    Elapsed time: 0.03s

"""
import collections
import requests
import tqdm

# 不要这样写 from countries.flags2_common import ...
from flags2_common import main, save_flag, HTTPStatus, Result

DEFAULT_CONCUR_REQ = 1
MAX_CONCUR_REQ = 1


def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = requests.get(url)
    # <1>get_flag 函数没有处理错误，当 HTTP 代码不是 200 时，使用 requests.Response.raise_for_status 方法抛出异常。
    if resp.status_code != 200:
        resp.raise_for_status()
    return resp.content


def download_one(cc, base_url, verbose=False):
    try:
        image = get_flag(base_url, cc)
    # <2>download_one 函数捕获 requests.exceptions.HTTPError 异常，特别处理 HTTP 404 错误……
    except requests.exceptions.HTTPError as exc:
        res = exc.response
        if res.status_code == 404:
            # <3>……方法是，把局部变量 status 设为 HTTPStatus.not_found；
            # HTTPStatus 是从 flags2_common 模块中导入的 Enum 对象。
            status = HTTPStatus.not_found
            msg = 'not found'
        else:  # <4>重新抛出其他 HTTPError 异常；这些异常会向上冒泡，传给调用方。
            raise
    else:
        save_flag(image, cc.lower() + '.gif')
        status = HTTPStatus.ok
        msg = 'OK'

    if verbose:  # <5>如果在命令行中设定了 -v/--verbose 选项，显示国家代码和状态消息；这就是详细模式中看到的进度信息。
        print(cc, msg)

    # <6>download_one 函数的返回值是一个 namedtuple————Result，其中有个 status 字段，
    # 其值是 HTTPStatus.not_found 或 HTTPStatus.ok。
    return Result(status, cc)


def download_many(cc_list, base_url, verbose, max_req):
    # <1>这个 Counter 实例用于统计不同的下载状态：HTTPStatus.ok、HTTPStatus.not_found 或 HTTPStatus.error。
    counter = collections.Counter()
    cc_iter = sorted(cc_list)  # <2>按字母顺序传入的国家代码列表，保存在 cc_iter 变量中。
    if not verbose:
        # <3>如果不是详细模式，把 cc_iter 传给 tqdm 函数，返回一个迭代器，产出 cc_iter 中的元素，还会显示进度条动画。
        cc_iter = tqdm.tqdm(cc_iter)
    for cc in cc_iter:  # <4>这个 for 循环迭代 cc_iter……
        try:
            res = download_one(cc, base_url, verbose)  # <5>……不断调用 download_one 函数，执行下载。
        # <6>处理 get_flag 函数抛出的与 HTTP 有关的且 download_one 函数没有处理的异常。
        except requests.exceptions.HTTPError as exc:
            error_msg = 'HTTP error {res.status_code} - {res.reason}'
            error_msg = error_msg.format(res=exc.response)
        # <7>处理其他与网络有关的异常。其他异常会中止这个脚本，因为调用 download_many 函数
        # 的 flags2_common.main 函数中没有 try/except 块。
        except requests.exceptions.ConnectionError as exc:
            error_msg = 'Connection error'
        else:  # <8>如果没有异常从 download_one 函数中逃出，从 download_one 函数返回的 namedtuple(HTTPStatus) 中获取 status。
            error_msg = ''
            status = res.status

        if error_msg:
            status = HTTPStatus.error  # <9>如果有错误，把局部变量 status 设为相应的状态。
        counter[status] += 1  # <10>以 HTTPStatus（一个 Enum）中的值为键，增加计数器。
        if verbose and error_msg:  # <11>如果是详细模式，而且有错误，显示带有当前国家代码的错误消息。
            print('*** Error for {}: {}'.format(cc, error_msg))

    return counter  # <12>返回 counter，以便 main 函数能在最终的报告中显示数量。


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
