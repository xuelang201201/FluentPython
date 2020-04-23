l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)  # list(l1) 创建 l1 的副本。
print(l2)
print(l2 == l1)  # 副本与源列表相等。
print(l2 is l1)  # 但是二者指代不同的对象。
