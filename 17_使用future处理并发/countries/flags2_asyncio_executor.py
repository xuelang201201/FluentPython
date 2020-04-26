"""使用默认的 ThreadPoolExecutor 对象运行 save_flag 函数"""

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


class FetchError(Exception):
    def __init__(self, country_code):
        self.country_code = country_code


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


async def download_one(session, cc, base_url, semaphore, verbose):
    try:
        async with semaphore:
            image = await get_flag(session, base_url, cc)
    except web.HTTPNotFound:
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        loop = asyncio.get_event_loop()  # <1>获取事件循环对象的引用。
        # <2>run_in_executor 方法的第一个参数是 Executor 实例；如果设为 None，使用事件循环的默认 ThreadPoolExecutor 参数。
        loop.run_in_executor(None,
                             save_flag, image, cc.lower() + '.gif')  # <3>余下的参数是可调用的对象，以及可调用对象的位置参数。
        status = HTTPStatus.ok
        msg = 'OK'

    if verbose and msg:
        print(cc, msg)

    return Result(status, cc)


async def downloader_coro(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concur_req)
    async with aiohttp.ClientSession() as session:  #
        to_do = [download_one(session, cc, base_url, semaphore, verbose)
                 for cc in sorted(cc_list)]

        to_do_iter = asyncio.as_completed(to_do)
        if not verbose:
            to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))
        for future in to_do_iter:
            try:
                res = await future
            except FetchError as exc:
                country_code = exc.country_code
                try:
                    error_msg = exc.__cause__.args[0]
                except IndexError:
                    error_msg = exc.__cause__.__class__.__name__
                if verbose and error_msg:
                    msg = '*** Error for {}: {}'
                    print(msg.format(country_code, error_msg))
                status = HTTPStatus.error
            else:
                status = res.status

            counter[status] += 1

    return counter


def download_many(cc_list, base_url, verbose, concur_req):
    loop = asyncio.get_event_loop()
    coro = downloader_coro(cc_list, base_url, verbose, concur_req)
    counts = loop.run_until_complete(coro)
    loop.close()

    return counts


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
