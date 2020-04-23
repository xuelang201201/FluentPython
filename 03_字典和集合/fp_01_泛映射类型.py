"""
collections.abc 模块中有 Mapping 和 MutableMapping 这两个抽象基类，
它们的作用是为 dict 和其他类似的类型定义形式接口。这些抽象基类的主要
作用是作为形式化的文档，它们定义了构建一个映射类型所需要的最基本的接口。
然后它们还可以跟 instance 一起被用来判定某个数据是不是广义上的映射类型。
"""

from collections import abc

my_dict = {}
# 用 instance 而不是 type 来检查某个参数是否为 dict 类型，
# 因为这个参数有可能不是 dict，而是一个比较另类的映射类型
print(isinstance(my_dict, abc.Mapping))  # 判断是不是广义上的映射类型
