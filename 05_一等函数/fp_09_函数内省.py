# 列出常规对象没有而函数有的属性


class C:
    pass  # 创建一个空的用户定义的类。


obj = C()  # 创建一个实例。


def func(): pass  # 创建一个空函数。


print(sorted(set(dir(func)) - set(dir(obj))))  # 计算差集，然后排序，得到类的实例没有而函数有的属性列表。
