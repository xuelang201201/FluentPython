from fp_14_twilight_bus import TwilightBus

basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']  # basketball_team 中有 5 个学生的名字。
bus = TwilightBus(basketball_team)  # 使用这队学生实例化 TwilightBus。
bus.drop('Tina')  # 一个学生从 bus 下车了，接着又有一个学生下车了。
bus.drop('Pat')
print(basketball_team)  # 下车的学生从篮球队中消失了。
