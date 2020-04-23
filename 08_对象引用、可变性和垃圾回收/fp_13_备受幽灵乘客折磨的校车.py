from fp_12_haunted_bus import HauntedBus

bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)  # 目前没什么问题，bus1 没有出现异常。
bus2 = HauntedBus()  # 一开始，bus2 是空的，因此把默认的空列表赋值给 self.passengers。
bus2.pick('Carrie')
print(bus2.passengers)
bus3 = HauntedBus()  # bus3 一开始也是空的，因此还是赋值默认的列表。
print(bus3.passengers)  # 但是默认列表不为空！
bus3.pick('Dave')
print(bus2.passengers)  # 登上 bus3 的 Dave 出现在 bus2 中。
print(bus2.passengers is bus3.passengers)  # 问题是，bus2.passengers 和 bus3.passengers 指代同一个列表。
print(bus1.passengers)  # 但 bus1.passengers 是不同的列表。
print(dir(HauntedBus.__init__))
print(HauntedBus.__init__.__defaults__)
print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)
