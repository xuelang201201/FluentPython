"""使用 asyncio 和 aiohttp 包实现的异步下载脚本"""

import os
import time
import sys
import asyncio  # <1>导入 asyncio 包。

import aiohttp  # <2>必须安装 aiohttp 包，它不在标准库中。

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = '/home/charlie/Downloads/'


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


async def get_flag(session, cc):  # <3>协程应该在 def 前使用 async。
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    # <4>阻塞的操作通过协程实现，客户代码通过 async with 把职责委托给协程，以便异步运行协程。
    async with session.get(url) as resp:
        return await resp.read()  # <5>读取响应内容是一项单独的异步操作。


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


async def download_one(session, cc):  # <6>download_one 函数也必须是协程，因为用到了 async。
    # <7>与依序下载版 download_one 函数唯一的区别是这一行中的 await；函数定义体中的其他代码与之前完全一样。
    image = await get_flag(session, cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


async def download_many(cc_list):
    async with aiohttp.ClientSession() as session:  # <8>
        res = await asyncio.gather(  # <9>
            *[asyncio.create_task(download_one(session, cc))
              for cc in sorted(cc_list)])

    return len(res)


def main():  # <10>运行协程
    t0 = time.time()
    count = asyncio.run(download_many(POP20_CC))
    elapsed = time.time() - t0
    msg = '\n{} flags download in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main()
