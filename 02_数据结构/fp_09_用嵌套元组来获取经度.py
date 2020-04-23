# 嵌套元组拆包
metro_areas = [
    # 每个元组内有4个元素，其中最后一个元素是一对坐标
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

# {:^9} 中间对齐（宽度9）
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
# 我们把输入元组的最后一个元素拆包到由变量构成的元组里，这里就获取了坐标
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:  # if longitude <= 0: 这个条件判断把输出限制在西半球的城市
        print(fmt.format(name, latitude, longitude))
