# 一个简单的类，说明可变默认值的危险
class HauntedBus:
    """备受幽灵乘客折磨的校车"""

    def __init__(self, passengers=[]):  # 如果没传入 passengers 参数，使用默认绑定的列表对象，一开始是空列表。
        # 这个赋值语句把 self.passengers 变成 passengers 的别名，而没有传入 passengers 参数时，后者又是默认列表的别名。
        self.passengers = passengers

    def pick(self, name):
        # 在 self.passengers 上调用 .remove() 和 .append() 方法时，修改的其实是默认列表，它是函数对象的一个属性。
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)
