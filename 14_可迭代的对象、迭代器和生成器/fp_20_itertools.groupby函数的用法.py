import itertools

print(list(itertools.groupby('LLLLAAGGG')))  # <1>groupby 函数产出 (key, group_generator) 这种形式的元组。
# [('L', <itertools._grouper object at 0x7f7b9c62c2b0>),
# ('A', <itertools._grouper object at 0x7f7b9c60adf0>),
# ('G', <itertools._grouper object at 0x7f7b9c60ae80>)]

# <2>处理 groupby 函数返回的生成器要嵌套迭代：这里在外层使用 for 循环，内层使用列表推导。
for char, group in itertools.groupby('LLLLAAAGG'):
    print(char, '->', list(group))
# L -> ['L', 'L', 'L', 'L']
# A -> ['A', 'A', 'A']
# G -> ['G', 'G']

animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear',
           'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len)  # <3>为了使用 groupby 函数，要排序输入；这里按照单词的长度排序。
print(animals)
# ['rat', 'bat', 'duck', 'bear', 'lion', 'eagle', 'shark', 'giraffe', 'dolphin']

for length, group in itertools.groupby(animals, len):  # <4>再次遍历 key 和 group 值对，把 key 显示出来，并把 group 扩展成列表。
    print(length, '->', list(group))
# 3 -> ['rat', 'bat']
# 4 -> ['duck', 'bear', 'lion']
# 5 -> ['eagle', 'shark']
# 7 -> ['giraffe', 'dolphin']

for length, group in itertools.groupby(reversed(animals), len):  # <5>这里使用 reverse 生成器从右向左迭代 animals。
    print(length, '->', list(group))
# 7 -> ['dolphin', 'giraffe']
# 5 -> ['shark', 'eagle']
# 4 -> ['lion', 'bear', 'duck']
# 3 -> ['bat', 'rat']
