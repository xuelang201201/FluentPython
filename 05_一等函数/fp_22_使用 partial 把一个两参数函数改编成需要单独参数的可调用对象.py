from operator import mul
from functools import partial

triple = partial(mul, 3)  # 使用 mul 创建 triple 函数，把第一个定位参数定为 3。
print(triple(7))  # 测试 triple 函数。
print(list(map(triple, range(1, 10))))  # 在 map 中使用 triple；在这个示例中不能使用 mul。
