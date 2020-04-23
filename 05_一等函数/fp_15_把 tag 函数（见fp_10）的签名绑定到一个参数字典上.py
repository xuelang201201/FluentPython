# tag 函数用于生产 HTML 标签；使用名为 cls 的关键字参数传入 “class” 属
# 性，这是一种变通方法，因为 “class” 是 Python 的关键字
import inspect


def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s<%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


sig = inspect.signature(tag)  # 获取 tag 函数的签名
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)  # 把一个字典参数传给 .bind() 方法。
print(bound_args)  # 得到一个 BoundArguments 对象。
# <BoundArguments (name='img', cls='framed', attrs={'title': 'Sunset Boulevard', 'src': 'sunset.jpg'})>
# 迭代 bound_args.arguments（一个OrderedDict对象）中的元素，显示参数的名称和值。
for name, value in bound_args.arguments.items():
    print(name, '=', value)
del my_tag['name']  # 把必须指定的参数 name 从 my_tag 中删除。
bound_args = sig.bind(**my_tag)  # 调用 sig.bind(**my_tag)，抛出 TypeError，抱怨缺少 name 参数。
