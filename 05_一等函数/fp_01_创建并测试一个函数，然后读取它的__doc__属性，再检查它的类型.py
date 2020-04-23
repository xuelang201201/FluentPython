# 把函数视作对象
def factorial(n):  # 这是一个控制台会话，因此我们是在“运行时”创建一个函数。
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(42))
print(factorial.__doc__)  # __doc__是函数对象众多属性中的一个。
print(type(factorial))  # factorial 是 function 类的实例。
