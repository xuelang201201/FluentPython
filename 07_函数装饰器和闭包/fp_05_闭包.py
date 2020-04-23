# 计算移动平均值的类
class Averager(object):
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))


# 计算移动平均值的高阶函数
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)  # series 是自由变量
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))

# 审查 make_averager 创建的函数
print(avg.__code__.co_varnames)  # 局部变量的名称
print(avg.__code__.co_freevars)  # 自由变量的名称

print(avg.__closure__)  # series 的绑定在返回的 avg 函数的 __closure__ 属性中。
# avg.__closure__ 中的各个元素对应于 avg.__code__.co_freevars 中的一个名称。
print(avg.__closure__[0].cell_contents)
# 这些元素是 cell 对象，有个 cell_contents 属性，保存着真正的值。
