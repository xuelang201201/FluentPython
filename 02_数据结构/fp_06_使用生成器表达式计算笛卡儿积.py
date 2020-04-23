colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# 生成器表达式逐个产出元素，从来不会一次性产出一个含有6个T恤样式的列表
for t_shirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(t_shirt)
