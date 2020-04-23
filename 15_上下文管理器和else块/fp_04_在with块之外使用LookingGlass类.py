from fp_01_mirror import LookingGlass

manager = LookingGlass()  # <1>实例化并审查 manager 实例。
print(manager)
# <fp_01_mirror.LookingGlass object at 0x7fa5d48ef760>
monster = manager.__enter__()  # <2>在上下文管理器上调用 __enter__() 方法，把结果存储在 monster 中。
# <3>monster 的值是字符串 'JABBERWOCKY'。打印出的 True 标识符是反向的，因为 stdout 的
# 所有输出都经过 __enter__ 方法中打补丁的 write 方法处理。
print(monster == 'JABBERWOCKY')
# eurT
print(monster)
# YKCOWREBBAJ
print(manager)
# >067fe84d5af7x0 ta tcejbo ssalGgnikooL.rorrim_10_pf<
manager.__exit__(None, None, None)  # <4>调用 manager.__exit__，还原成之前的 stdout.write。
print(monster)
# JABBERWOCKY
