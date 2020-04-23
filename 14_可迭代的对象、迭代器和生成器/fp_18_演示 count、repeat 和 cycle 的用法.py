import itertools
import operator

ct = itertools.count()  # 使用 count 函数构建 ct 生成器。
print(next(ct))  # 获取 ct 中的地一个元素。
# 0
print(next(ct), next(ct), next(ct))  # 不能使用 ct 构建列表，因为 ct 是无穷的，所以我获取接下来的 3 个元素。
# 1 2 3
# 如果使用 islice 或 takewhile 函数做了限制，可以从 count 生成器中构建列表。
print(list(itertools.islice(itertools.count(1, .3), 3)))
# [1, 1.3, 1.6]
cy = itertools.cycle('ABC')  # 使用 'ABC' 构建一个 cycle 生成器，然后获取第一个元素————'A'。
print(next(cy))
# A
print(list(itertools.islice(cy, 7)))  # 只要受到 islice 函数的限制，才能构建列表；这里获取接下来的 7 个元素。
# ['B', 'C', 'A', 'B', 'C', 'A', 'B']
rp = itertools.repeat(7)  # 构建一个 repeat 生成器，始终产出数字 7。
print(next(rp), next(rp))
# 7 7
print(list(itertools.repeat(8, 4)))  # 传入 times 参数可以限制 repeat 生成器生成的元素数量：这里会生成 4 次数字 8。
# [8, 8, 8, 8]
# repeat 函数的常见用途：为 map 函数提供固定参数，这里提供的是乘数 5。
print(list(map(operator.mul, range(11), itertools.repeat(5))))
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
