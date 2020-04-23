class MySeq:
    def __getitem__(self, index):
        return index  # 在这个示例中，__getitem__直接返回传给它的值。


s = MySeq()
print(s[1])  # 单个索引，没什么新奇的。
print(s[1:4])  # 1:4 表示法变成了 slice(1, 4, None)。
print(s[1:4:2])  # slice(1, 4, 2) 的意思是从 1 开始，到 4 结束，步幅为 2。
print(s[1:4:2, 9])  # 神奇的事发生了：如果 [] 中有逗号，那么 __getitem__ 收到的是元组。
print(s[1:4:2, 7:9])  # 元组中甚至可以有多个切片对象。
