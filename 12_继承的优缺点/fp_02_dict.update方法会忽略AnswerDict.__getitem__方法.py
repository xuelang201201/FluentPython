class AnswerDict(dict):
    def __getitem__(self, key):  # 不管传入什么键，AnswerDict.__getitem__ 方法始终返回 42。
        return 42


ad = AnswerDict(a='foo')  # ad 是 AnswerDict 的实例，以 ('a', 'foo') 键值对初始化。
print(ad['a'])  # ad['a'] 返回 42，这与预期相符。
d = {}
d.update(ad)  # d 是 dict 的实例，使用 ad 中的值更新 d。
print(d['a'])  # dict.update 方法忽略了 AnswerDict.__getitem__ 方法。
print(d)
