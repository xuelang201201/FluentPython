colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# 这里得到的结果是先以颜色排列，再以尺码排列
t_shirts = [(color, size) for color in colors for size in sizes]
print(t_shirts)

# 注意，这里两个循环的嵌套关系和上面列表推导中 for 从句的先后顺序一样
for color in colors:
    for size in sizes:
        print((color, size))

# 如果想依照先尺码后颜色的顺序来排列，只需要调整从句的顺序
t_shirts = [(color, size) for size in sizes for color in colors]
print(t_shirts)
