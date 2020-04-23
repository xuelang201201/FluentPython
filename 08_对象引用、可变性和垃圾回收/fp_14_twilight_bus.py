class TwilightBus:
    """让乘客销声匿迹的校车"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []  # 这里谨慎处理，当 passengers 为 None 时，创建一个新的空列表。
        else:
            # 然而，这个赋值语句把 self.passengers 变成 passengers 的别名，
            # 而后者是传给 __init__ 方法的实参（即fp_15中的 basketball_team）的别名。
            self.passengers = list(passengers)  # 创建 passengers 列表的副本；如果不是列表，就把它转换成列表。

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        # 在 self.passengers 上调用 .remove() 和 .append() 方法其实会修改传给构造方法的那个列表。
        self.passengers.remove(name)
