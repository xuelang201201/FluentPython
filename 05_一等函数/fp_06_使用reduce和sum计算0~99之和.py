from functools import reduce  # 从 Python 3.0 起，reduce 不再是内置函数了。
from operator import add  # 导入 add，以免创建一个专求两数之和的函数。

reduce_result = reduce(add, range(100))  # 计算 0~99 之和。
print(reduce_result)
sum_result = sum(range(100))  # 使用 sum 做相同的求和；无需导入或创建求和函数。
print(sum_result)
