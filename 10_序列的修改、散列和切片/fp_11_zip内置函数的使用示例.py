from itertools import zip_longest

print(zip(range(3), 'ABC'))  # zip 函数返回一个生成器，按需生成元组。
# <zip object at 0x7f397d6dc440>
print(list(zip(range(3), 'ABC')))  # 为了输出，构建一个列表；通常，我们会迭代生成器。
# [(0, 'A'), (1, 'B'), (2, 'C')]
print(list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3])))  # zip 有个奇怪的特性：当一个可迭代对象耗尽后，它不发出警告就停止。
# [(0, 'A', 0.0), (1, 'B', 1.1), (2, 'C', 2.2)]

# itertools.zip_longest 函数的行为有所不同：使用可选的 fillvalue (默认值为None) 填充缺失的值，
# 因此可以继续产出，直到最长的可迭代对象耗尽。
print(list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1)))
# [(0, 'A', 0.0), (1, 'B', 1.1), (2, 'C', 2.2), (-1, -1, 3.3)]
