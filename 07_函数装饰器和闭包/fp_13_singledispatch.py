# singledispatch 创建一个自定义的 htmlize.register 装饰器，把多个函数绑在一起组成一个泛函数
from functools import singledispatch
from collections import abc
import numbers
import html


# functools.singledispatch 装饰器可以把整体方案拆分成多个模块，甚至可以为你无法修改的类提供专门的函数。使用
# @singledispatch 装饰的普通函数会变成泛函数（generic
# function）:根据第一个参数的类型，以不同方式执行相同操作的一组函数。
@singledispatch  # @singledispatch 标记处理 object 类型的基函数。
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)  # 各个专门函数使用 @<<base_function>>.register(<<type>>) 装饰。
def _(text):  # 专门函数的名称无关紧要：_是个不错的选择，简单明了。
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


# 为每个需要特殊处理的类型注册一个函数。numbers.Integral 是 int 的虚拟超类。
@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)  # 可叠放多个 register 装饰器，让同一个函数支持不同类型。
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '<li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '<li>\n</ul>'
