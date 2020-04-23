import copy
from fp_08_校车乘车途中上车和下车 import Bus

bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))  # 使用 copy 和 deepcopy，创建 3 个不同的 Bus 实例。
bus1.drop('Bill')
print(bus2.passengers)
# ['Alice', 'Claire', 'David']  # bus1 中的 'Bill' 下车后，bus2 中也没有他了。
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
# 审查 passengers 属性后，bus1 和 bus2 共享同一个列表对象，因为 bus2 是 bus1 的浅复制副本。
# 140185405933248 140185405933248 140185405935360
print(bus3.passengers)
# ['Alice', 'Bill', 'Claire', 'David']  # bus3 是 bus1 的深复制副本，因此它的 passengers 属性指代另一个列表。
