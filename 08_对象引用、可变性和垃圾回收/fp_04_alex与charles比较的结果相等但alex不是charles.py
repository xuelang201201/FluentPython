"""
每个变量都有标识、类型和值。对象一旦创建，它的标识绝不会变；你可以把标识理解为对象在内存中的地址。
is 运算符比较两个对象的标识；id() 函数返回对象表示的整数表示。
"""

from fp_03_charles和lewis指代同一个对象 import charles
alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}  # alex 指代的对象与赋值给 charles 的对象内容一样。
print(alex == charles)  # 比较两个对象，结果相等，这是因为 dict 类的 __eq__ 方法就是这样实现的。
print(alex is not charles)  # 但它们是不同的对象。这是 Python 说明标识不同的方式：a is not b。
