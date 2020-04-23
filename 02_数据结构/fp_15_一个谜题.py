# 一个关于+=的谜题
t = (1, 2, [30, 40])
t[2] += [50, 60]

# 到底会发生下面4中情况中的哪一种？

# a. t变成 (1, 2, [30, 40, 50, 60])。
# b. 因为 tuple 不支持对它的元素赋值，所以会抛出 TypeError 异常。
# c. 以上两个都不是。
# d. a 和 b 都是对的。

# 在终端中运行：没人料到的结果：t[2] 被改动了，但是也有异常抛出
# t
# TypeError               Traceback (most recent call last)
# <ipython-input-2-d877fb0e9d36> in <module>
# ----> 1 t[2] += [50, 60]
#
# TypeError: 'tuple' object does not support item assignment
# t
# (1, 2, [30, 40, 50, 60])

# 所以答案是 d
