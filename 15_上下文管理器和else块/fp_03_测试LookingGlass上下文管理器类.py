from fp_01_mirror import LookingGlass

# <1>上下文管理器是 LookingGlass 类的实例；Python 在上下文管理器上调
# 用 __enter__ 方法，把返回结果绑定到 what 上。
with LookingGlass() as what:
    print('Alice, Kitty and Snowdrop')  # <2>打印一个字符串，然后打印 what 变量的值。
    print(what)
# pordwonS dna yttiK ,ecilA  # <3>打印出的内容是反向的。
# YKCOWREBBAJ
# <4>现在，with 块已经执行完毕。可以看出，__enter__ 方法返
# 回的值————即存储在 what 变量中的值————是字符串 'JABBERWOCKY'。
print(what)
# JABBERWOCKY
print('Back to normal.')  # <5> 输出不再是反向的了。
# Back to normal.
