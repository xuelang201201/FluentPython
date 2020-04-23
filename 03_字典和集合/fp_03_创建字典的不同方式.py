a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个
# 元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
# 我们可以使用 list() 转换来输出列表。如果各个迭代器的元素个数不一致，
# 则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

print("a = " + str(a))
print("b = " + str(b))
print("c = " + str(c))
print("d = " + str(d))
print("e = " + str(e))
print(a == b == c == d == e)
