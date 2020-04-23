# 把字符串和字节序列参数传给 listdir 函数得到的结果
import os

print(os.listdir('.'))  # 第三个文件名是 “digits-of-π.txt”
print(os.listdir(b'.'))  # 参数是字节序列，listdir 函数返回的文件名也是字节序列：b'\xcf\x80' 是希腊字母 π 的 UTF-8 编码。
