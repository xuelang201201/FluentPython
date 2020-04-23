import itertools
import operator

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(list(itertools.accumulate(sample)))  # 计算总和。
# [5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
print(list(itertools.accumulate(sample, min)))  # 计算最小值。
# [5, 4, 2, 2, 2, 2, 2, 0, 0, 0]
print(list(itertools.accumulate(sample, max)))  # 计算最大值。
# [5, 5, 5, 8, 8, 8, 8, 8, 9, 9]
print(list(itertools.accumulate(sample, operator.mul)))  # 计算乘积。
# [5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0]
print(list(itertools.accumulate(range(1, 11), operator.mul)))  # 从 1! 到 10!，计算各个数的阶乘。
# [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
