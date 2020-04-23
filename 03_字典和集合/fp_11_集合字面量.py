from dis import dis

# 除空集之外，集合的字面量————{1}、{1, 2}，等等————看起来跟它的数学形式一模一样。
# 如果是空集，那么必须写成 set() 的形式。
# 句法的陷阱
# 不要忘了，如果要创建一个空集，你必须用不带任何参数的构造方法 set()。
# 如果只是写成 {} 的形式，跟以前一样，你创建的其实是个空字典。

# 在 Python3 里面，除了空集，集合的字符串表示形式总是以 {...} 的形式出现。
s = {1}
print(type(s))
print(s)
print(s.pop())
print(s)

# 用 dis.dis (反汇编函数) 来看看两个方法的字节码的不同：
dis('{1}')  # 检查 {1} 字面量背后的字节码。
# 1        0 LOAD_CONST         0 (1)
#          2 BUILD_SET          1   # 特殊的字节码 BUILD_SET 几乎完成了所有的工作。
#          4 RETURN_VALUE

dis('set([1])')  # set([1]) 的字节码。
# 1        0 LOAD_NAME          0 (set)  # 3 种不同的操作代替了上面的 BUILD_SET: LOAD_NAME、BUILD_LIST 和 CALL_FUNCTION。
#          2 LOAD_CONST         0 (1)
#          4 BUILD_LIST         1
#          6 CALL_FUNCTION      1
#          8 RETURN_VALUE

print(frozenset(range(10)))
