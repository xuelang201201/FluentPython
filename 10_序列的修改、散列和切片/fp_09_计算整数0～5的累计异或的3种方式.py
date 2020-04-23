import functools
import operator

n = 0
for i in range(1, 6):  # 使用 for 循环和累加器变量计算聚合异或。
    n ^= i
print(n)

result1 = functools.reduce(lambda a, b: a ^ b, range(6))  # 使用 functools.reduce 函数，传入匿名函数。
print(result1)

result2 = functools.reduce(operator.xor, range(6))  # 使用 functools.reduce 函数，把 lambda 表达式换成 operator.xor。
print(result2)
