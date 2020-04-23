import os

fp = open('cafe.txt', 'w', encoding='utf_8')
print(fp)  # 默认情况下，open 函数采用文本模式，返回一个TextIOWrapper 对象。

print(fp.write('café'))  # 在 TextIOWrapper 对象上调用 write 方法返回写入的 Unicode 字符数。

fp.close()

size = os.stat('cafe.txt').st_size  # os.stat 报告文件中有 5 个字节；UTF-8 编码的 'é' 占两个字节，0xc3 和 0xa9。
print(size)

fp2 = open('cafe.txt')
print(fp2)  # 打开文本文件时没有显示指定编码，返回一个 TextIOWrapper 对象，编码是区域设置中的默认值。

print(fp2.encoding)  # TextIOWrapper 对象有个 encoding 属性；查看它，发现这里的编码是 cp936。

print(fp2.read())
# 'caf茅'  # 在 Windows cp936 编码中，0xc3 字节是 “茅”，0xa9 字节是版权符号。

fp3 = open('cafe.txt', encoding='utf_8')  # 使用正确的编码打开那个文件。
print(fp3)
print(fp3.read())
# café  # 结果符合预期：得到的是四个 Unicode 字符 'café'。

fp4 = open('cafe.txt', 'rb')  # 'rb' 标志指明在二进制模式中读取文件。
print(fp4)
# <_io.BufferedReader name='cafe.txt'>  # 返回的是 BufferedReader 对象，而不是 TextIOWrapper 对象。

print(fp4.read())  # 读取返回的字节序列，结果与预期相符。
