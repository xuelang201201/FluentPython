# 计算移动平均值的高阶函数，不保存所有历史值，但有缺陷。
# def make_averager():
#     count = 0
#     total = 0
#
#     def averager(new_value):
#         count += 1
#         total += new_value
#         return total / count
#
#     return averager
#
#
# avg = make_averager()
# print(avg(10))


# Traceback (most recent call last):
# ...
# UnboundLocalError: local variable 'count' referenced before assignment

# 问题是，当 count 是数字或任何不可变类型时， count += 1 语句的作用其实与 count = count + 1 一样。因此，
# 我们在 averager 的定义中为 count 赋值了，这会把 count 变成局部变量。total变量也受这个问题影响。

# 计算移动平均值，不保存所有历史（使用 nonlocal 修正）
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager()
print(avg(10))
