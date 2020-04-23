import struct

fmt = '<3s3sHH'  # 结构体的格式：< 是小字节序，3s3s 是两个 3 字节序列，HH 是两个 16 位二进制整数。
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())  # 使用内存中的文件内容创建一个 memoryview 对象……
header = img[:10]  # ……然后使用它的切片再创建一个 memoryview 对象；这里不会复制字节序列。
print(bytes(header))  # 转换成字节序列，这只是为了显示；这里复制了 10 字节。
print(struct.unpack(fmt, header))  # 拆包 memoryview 对象，得到一个元组，包含类型、版本、宽度和高度。
del header  # 删除引用，释放 memoryview 实例所占的内存。
del img
