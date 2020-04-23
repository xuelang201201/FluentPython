import collections


# 子类化 UserDict
class StrKeyDict(collections.UserDict):  # StrKeyDict 是对 UserDict 的扩展。

    def __missing__(self, key):  # __missing__ 跟示例 fp_07 里的一模一样。
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        # __contains__ 则更简洁些。这里可以放心假设所有已经存储的键都是字符串。因此，
        # 只要在 self.data 上查询就好了，并不需要像 StrKeyDict0 那样去麻烦 self.keys()。
        return str(key) in self.data

    def __setitem__(self, key, item):
        # __setitem__ 会把所有的键都转换成字符串。由于把具体的实现委托给了 self.data 属
        # 性，这个方法写起来也不难。
        self.data[str(key)] = item


d = StrKeyDict([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])
# print(d[1])

print(d.get('2'))
print(d.get('4'))
print(d.get(1, 'N/A'))

print(2 in d)
print(1 in d)
