from collections import namedtuple
# 创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字。
# 后者可以是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串。
City = namedtuple('City', 'name country population coordinates')

# 存放在对应字段里的数据要以一串参数的形式传入到构造函数中
# （注意，元组的构造函数却只接受单一的可迭代对象）
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)

# 可以通过字段名或者位置来获取一个字段的信息
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])


# 具名元组的属性和方法
print(City._fields)  # _fields 属性是一个包含这个类所有字段名称的元组
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

# 用 _make() 通过接受一个可迭代对象来生成这个类的一个实例，它的作用跟
# City(*delhi_data) 是一样的
delhi = City._make(delhi_data)
print(delhi)

# _asdict() 把具名元组以 collections.OrderedDict 的形式返回，
# 我们可以利用它来把元组里的信息友好地呈现出来
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ':', value)
