"""依序下载的脚本，另外两个脚本会重用其中几个函数"""

import os
# <1>导入 requests 库。这个库不在标准库中，因此依照惯例，在导入标准库中的
# 模块（os、time 和 sys）之后导入，而且使用一个空行分隔开。
import requests
import sys
import time

# <2>列出人口最多的 20 个国家的 ISO 3166 国家代码，按照人口数量降序排列。
POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'  # <3>获取国旗图像的网站。

DEST_DIR = '/home/charlie/Downloads/'  # <4>保存图像的本地目录。


def save_flag(img, filename):  # <5>把 img（字节序列）保存到 DEST_DIR 目录中，命名为 filename。
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):  # <6>指定国家代码，构建 URL，然后下载图像，返回响应中的二进制内容。
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


# <7>显示一个字符串，然后刷新 sys.stdout，这样能在一行消息中看到进度。在 Python 中
# 得这么做，因为正常情况下，遇到换行才会刷新 stdout 缓冲。
def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):  # <8>download_many 是与并发实现比较的关键函数。
    for cc in sorted(cc_list):  # <9>按字母表顺序迭代国家代码列表，明确表明输出的顺序与输入一致。返回下载的国旗数量。
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')

    return len(cc_list)


def main():  # <10>main 函数记录并报告运行 download_many 函数之后的耗时。
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    # <11>main 函数必须调用执行下载的函数；我们把 download_many 函数当作参数传给 main 函数，
    # 这样 main 函数可以用作库函数，在后面的示例中接收 download_many 函数的其他实现。
    main()
