class DoppelDict(dict):
    def __setitem__(self, key, value):
        # DoppelDict.__setitem__ 方法会重复存入的值（只是为了提供易于观察的效果）。它把职责委托给超类。
        super(DoppelDict, self).__setitem__(key, [value] * 2)


dd = DoppelDict(one=1)  # 继承自 dict 的 __init__ 方法显然忽略了我们覆盖的 __setitem__ 方法：'one' 的值没有重复。
print(dd)
dd['two'] = 2  # [] 运算符会调用我们覆盖的 __setitem__ 方法，按预期那样工作：'two' 对应的是两个重复的值，即 [2, 2]。
print(dd)
dd.update(three=3)  # 继承自 dict 的 update 方法也不使用我们覆盖的 __setitem__ 方法：'three' 的值没有重复。
print(dd)
