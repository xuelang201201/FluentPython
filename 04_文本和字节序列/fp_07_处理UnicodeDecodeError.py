"""把字节序列解码成字符串：成功和错误处理"""

# 这些字节序列是使用 latin1 编码的 “Montréal”；'\xe9' 字节对应 “é”。
octets = b'Montr\xe9al'

# 可以使用 'cp1252' (Windows 1252) 解码，因为它是 latin1 的有效超集。
print(octets.decode('cp1252'))

# ISO-8859-7 用于编码希腊文，因此无法正确解释 '\xe9' 字节，而且没有抛出错误。
print(octets.decode('iso8859_7'))

# KOI8-R 用于编码俄文；这里，'\xe9' 表示西里尔字母 “И”。
print(octets.decode('koi8_r'))

# 'utf_8' 编解码器检测到 octets 不是有效的 UTF-8 字符串，抛出 UnicodeDecodeError。
# print(octets.decode('utf_8'))

# 使用 'replace' 错误处理方式，\xe9 替换成了 “�” (码位是 U+FFFD)，这是官方指定
# 的 REPLACEMENT CHARACTER (替换字符)，表示未知字符。
print(octets.decode('utf_8', errors='replace'))
