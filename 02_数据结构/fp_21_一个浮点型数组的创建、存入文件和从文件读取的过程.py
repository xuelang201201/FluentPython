# 如果我们需要一个只包含数字的列表，那么 array.array 比 list 更高效。数组支持所有跟
# 可变序列有关的操作，包括 .pop、.insert 和 .extend。另外，数组还提供从文件读取和存
# 入文件的更快方法，如 .frombytes 和 .tofile。

from array import array  # 引入 array 类型
from random import random

# 利用一个可迭代对象来建立一个双精度浮点数组（类型码是'd'）,
# 这里我们用的可迭代对象是一个生成器表达式。
floats = array('d', (random() for i in range(10 ** 7)))
print(floats[-1])  # 查看数组的最后一个元素
fp = open('floats.bin', 'wb')
floats.tofile(fp)  # 把数组存入一个二进制文件里
fp.close()
floats2 = array('d')  # 新建一个双精度浮点空数组
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10 ** 7)  # 把1000万个浮点数从二进制文件里读取出来
fp.close()
print(floats2[-1])  # 查看新数组的最后一个元素
print(floats2 == floats)  # 检查两个数组的内容是不是完全一样
