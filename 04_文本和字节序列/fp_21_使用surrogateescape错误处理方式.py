# 在 Unix 衍生平台中，这些函数使用 surrogateescape 错误处理方式以避免遇到意外字节序列时卡住。
import os

print(os.listdir('.'))  # 列出目录里的文件，有个文件名中包含非 ASCII 字符。
print(os.listdir(b'.'))  # 假设我们不知道编码，获取文件名的字节序列形式。
pi_name_bytes = os.listdir(b'.')[3]  # pi_names_bytes 是包含 π 的文件名。
# 使用 'ascii' 编解码器和 'surrogateescape' 错误处理方式把它解码成字符串。
pi_name_str = pi_name_bytes.decode('ascii', 'surrogateescape')
print(pi_name_str)  # 各个非 ASCII 字节替换成代替码位：'\xcf\x80' 变成了 '\udccf\udc80'。
print(pi_name_str.encode('ascii', 'surrogateescape'))  # 编码成 ASCII 字节序列：各个代替码位还原成被替换的字节。
