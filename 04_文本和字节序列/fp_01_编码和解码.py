s = 'café'
print(len(s))  # 'café' 字符串有 4 个 Unicode 字符。

b = s.encode('utf8')  # 使用 UTF-8 把 str 对象编码成 bytes 对象。
print(b)
# b'caf\xc3\xa9'  # bytes 字面量以 b 开头。

print(len(b))  # 字节序列 b 有 5 个字节（在 UTF-8 中，“é” 的码位编码成两个字节）。

print(b.decode('utf8'))  # 使用 UTF-8 把 bytes 对象解码成 str 对象。
