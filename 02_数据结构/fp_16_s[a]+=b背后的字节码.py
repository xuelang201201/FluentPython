import dis

dis.dis('s[a] += b')
"""
1             0 LOAD_NAME                0 (s)
              2 LOAD_NAME                1 (a)
              4 DUP_TOP_TWO
              6 BINARY_SUBSCR   # 将s[a]的值存入 TOS（Top of Stack，栈的顶端）。
              8 LOAD_NAME                2 (b)
             10 INPLACE_ADD     # 计算 TOS += b。这一步能够完成，是因为 TOS 指向的是一个可变对象（也就是fp_15里的列表）。
             12 ROT_THREE
             14 STORE_SUBSCR    # s[a] = TOS 赋值。这一步失败，是因为 s 是不可变的元组（fp_15中的元组 t）。
             16 LOAD_CONST               0 (None)
             18 RETURN_VALUE
"""

# 不要把可变对象放在元组里面。
# 增量赋值不是一个原子操作。我们刚才也看到了，它虽然抛出了异常，但还是完成了操作。
# 查看 Python 的字节码并不难，而且它对我们了解代码背后的运行机制很有帮助。
