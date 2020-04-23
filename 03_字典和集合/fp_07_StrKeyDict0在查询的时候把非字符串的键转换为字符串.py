class StrKeyDict0(dict):  # StrKeyDict0 继承了 dict。

    def __missing__(self, key):
        if isinstance(key, str):  # 如果找不到的键本身就是字符串，那就抛出 KeyError 异常。
            raise KeyError(key)
        return self[str(key)]  # 如果找不到的键不是字符串，那么把它转换成字符串再进行查找。

    def get(self, key, default=None):
        try:
            # get 方法把查找工作用 self[key] 的形式委托给 __getitem__，
            # 这样在宣布查找失败之前，还能通过 __missing__ 再给某个键一个机会。
            return self[key]
        except KeyError:
            # 如果抛出 KeyError，那么说明 __missing__ 也失败了，于是返回 default。
            return default

    def __contains__(self, key):
        # 先按照传入键的原本的值来查找（我们的映射类型中可能含有非字符串的键），
        # 如果没找到，再用 str() 方法把键转换成字符串再查找一次。
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])
# print(d[1])

print(d.get('2'))
print(d.get('4'))
print(d.get(1, 'N/A'))

print(2 in d)
print(1 in d)
