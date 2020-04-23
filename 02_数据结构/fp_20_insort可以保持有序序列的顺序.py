# 用bisect.insort插入新元素
import bisect
import random

SIZE = 7

# random.seed() 会改变随机生成器的种子；传入的数值用于指定随机数生成时所用算法开始时所选定的整数值，
# 如果使用相同的seed()值，则每次生成的随机数都相同；如果不设置这个值，则系统会根据时间来自己选择这个值，
# 此时每次生成的随机数会因时间的差异而有所不同。
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
