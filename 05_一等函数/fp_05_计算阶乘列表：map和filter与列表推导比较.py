# 把函数视作对象
def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial

print(list(map(fact, range(6))))  # 构建 0! 和 5! 的一个阶乘列表。

print([fact(n) for n in range(6)])  # 使用列表推导执行相同的操作。

# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，
# 最后将返回 True 的元素放到新列表中。
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))  # 使用 map 和 filter 计算直到 5! 的奇数阶乘列表。

print([factorial(n) for n in range(6) if n % 2])  # 使用列表推导做相同的工作，换掉 map 和 filter，并避免了使用 lambda 表达式。
