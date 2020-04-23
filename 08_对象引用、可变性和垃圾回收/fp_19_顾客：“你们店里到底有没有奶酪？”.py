import weakref
from fp_18_cheese import Cheese

stock = weakref.WeakValueDictionary()  # stock 是 WeakValueDictionary 实例。
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
           Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese  # stock 把奶酪的名称映射到 catalog 中 Cheese 实例的弱引用上。

print(sorted(stock.keys()))
# ['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']  # stock 是完整的。
del catalog
print(sorted(stock.keys()))
# ['Parmesan']  # 删除 catalog 之后，stock 中的大多数奶酪都不见了，这是 WeakValueDictionary 的预期行为。为什么不是全部呢？
del cheese
print(sorted(stock.keys()))
# []

"""
为什么不是全部呢？

临时变量引用了对象，这可能会导致该变量的存在时间比预期长。通常，这对局部变量来说不是问题，因为它们在函数返回时会被销毁。
但是 for 循环中的变量 cheese 是全局变量，除非显示删除，否则不会消失。 
"""
