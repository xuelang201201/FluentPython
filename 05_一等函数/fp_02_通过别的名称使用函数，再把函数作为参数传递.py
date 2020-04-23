# 把函数视作对象
def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial
print(fact)
print(fact(5))
print(map(factorial, range(11)))
# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
print(list(map(fact, range(11))))
