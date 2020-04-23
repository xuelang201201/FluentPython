"""
bisect(haystack, needle) 在 haystack（干草垛）里搜索 needle（针）的位置，该位置满足的条件是，
把 needle 插入这个位置之后，haystack 还能保持升序。也就是说这个函数返回的位置前面的值，都小于
或等于 needle 的值。其中 haystack 必须是一个有序的序列。你可以先用 bisect(haystack, needle)
查找位置 index，再用 haystack.insert(index, needle)来插入新值。但你也可用 insort 来一步到位，
并且后者的速度更快一些。
"""

import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # 用特定的bisect函数来计算元素应该出现的位置
        offset = position * '  |'  # 利用该位置来算出需要几个分隔符号
        print(ROW_FMT.format(needle, position, offset))  # 把元素和其应该出现的位置打印出来


if __name__ == '__main__':

    # print(sys.argv[-1])  # E:/Python/Code/Fluent Python/02_数据结构/fp_18_在有序序列中用bisect查找某个元素的插入位置.py
    if sys.argv[-1] == 'left':  # 根据命令上最后一个参数来选用bisect函数
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)  # 把选定的函数在抬头打印出来
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
