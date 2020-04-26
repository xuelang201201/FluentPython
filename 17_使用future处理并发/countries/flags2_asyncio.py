"""使用 asyncio.as_completed 函数
"""

import asyncio
import collections

import aiohttp
from aiohttp import web
import tqdm

from flags2_common import main, HTTPStatus, Result, save_flag

# 默认设为较小的值，防止远程网站出错
# 例如503 - Service Temporarily Unavailable
DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000


class FetchError(Exception):  # <1>这个自定义的异常用于包装其他 HTTP 或网络异常，并获取 country_code，以便报告错误。
    def __init__(self, country_code):
        self.country_code = country_code


# <2>get_flag 协程有三种返回结果：返回下载得到的图像；HTTP 响应码为 404 时，抛出 web.HTTPNotFound 异常；
# 返回其他 HTTP 状态码时，抛出 aiohttp.HttpProcessingError 异常。
async def get_flag(session, base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    async with session.get(url) as resp:
        if resp.status == 200:
            return await resp.read()
        elif resp.status == 404:
            raise web.HTTPNotFound()
        else:
            raise aiohttp.HttpProcessingError(
                code=resp.status, message=resp.readon,
                headers=resp.headers)


# <3>semaphore 参数是 asyncio.Semaphore 类（https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore）
# 的实例。Semaphore 类是同步装置，用于限制并发请求数量。
async def download_one(session, cc, base_url, semaphore, verbose):
    try:
        # <4>在 async with 表达式中把 semaphore 当成上下文管理器使用，防止阻塞整个系统：如果
        # semaphore 计数器的值是所允许的最大值，只有这个协程会阻塞。
        async with semaphore:
            # <5>退出这个 async with 语句后，semaphore 计数器的值会递减，解除阻塞可能在等待同一个
            # semaphore 对象的其他协程实例。
            image = await get_flag(session, base_url, cc)
    except web.HTTPNotFound:  # <6>如果没找到国旗，相应地设置 Result 的状态。
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as exc:
        # <7>其他异常当作 FetchError 抛出，传入国家代码，并使用 “PEP 3134 —— Exception
        # Chaining and Embedded Tracebacks”（https://www.python.org/dev/peps/pep-3134/）
        # 引入的 raise X from Y 句法链接原来的异常。
        raise FetchError(cc) from exc
    else:
        save_flag(image, cc.lower() + '.gif')  # <8>这个函数的作用是把国旗文件保存到硬盘中。
        status = HTTPStatus.ok
        msg = 'OK'

    if verbose and msg:
        print(cc, msg)

    return Result(status, cc)


# <1>这个协程的参数与 download_many 函数一样，但是不能直接调用，因为它是协程函数，
# 而不是像 download_many 那样的普通函数。
async def downloader_coro(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    # <2>创建一个 asyncio.Semaphore 实例，最多允许激活 concur_req 个使用这个计数器的协程。
    semaphore = asyncio.Semaphore(concur_req)
    async with aiohttp.ClientSession() as session:  #
        to_do = [download_one(session, cc, base_url, semaphore, verbose)
                 for cc in sorted(cc_list)]  # <3>多次调用 download_one 协程，创建一个协程对象列表。

        to_do_iter = asyncio.as_completed(to_do)  # <4>获取一个迭代器，这个迭代器会在 future 运行结束后返回 future。
        if not verbose:
            to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))  # <5>把迭代器传给 tqdm 函数，显示进度。
        # <6>迭代运行结束的 future；这个循环与 flag2_threadpool.py 中 download_many 函数里的那个十分相似。
        # 不同的部分主要是异常处理，因为两个 HTTP 库（requests 和 aiohttp）之间有差异。
        for future in to_do_iter:
            try:
                # <7>获取 asyncio.Future 对象的结果，最简单的方法是使用 await，而不是调用 future.result() 方法。
                res = await future
            except FetchError as exc:  # <8>download_one 函数抛出的各个异常都包装在 FetchError 对象里，并且链接原来的异常。
                country_code = exc.country_code  # <9>从 FetchError 异常中获取错误发生时的国家代码。
                try:
                    error_msg = exc.__cause__.args[0]  # <10>尝试从原来的异常（__cause__）中获取错误消息。
                except IndexError:
                    # <11>如果原来的异常中找不到错误消息，使用所链接异常的类名作为错误消息。
                    error_msg = exc.__cause__.__class__.__name__
                if verbose and error_msg:
                    msg = '*** Error for {}: {}'
                    print(msg.format(country_code, error_msg))
                status = HTTPStatus.error
            else:
                status = res.status

            counter[status] += 1  # <12>记录结果。

    return counter  # <13>与其他脚本一样，返回计数器。


def download_many(cc_list, base_url, verbose, concur_req):
    loop = asyncio.get_event_loop()
    coro = downloader_coro(cc_list, base_url, verbose, concur_req)
    # <14>download_many 函数只是实例化 downloader_coro 协程，然后通过 run_until_complete 方法把它传给事件循环。
    counts = loop.run_until_complete(coro)
    loop.close()  # <15>所有工作做完后，关闭事件循环，返回 counts。

    return counts


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
