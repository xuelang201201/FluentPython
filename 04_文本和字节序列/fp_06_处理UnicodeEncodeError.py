"""编码成字节序列：成功和错误处理"""
city = 'São Paulo'

# 'utf_?' 编码能处理任何字符串。
encode_utf_8 = city.encode('utf_8')
print(encode_utf_8)

encode_utf_16 = city.encode('utf_16')
print(encode_utf_16)

# 'iso8859_1' 编码也能处理字符串 'São Paulo'。
encode_iso8859_1 = city.encode('iso8859_1')
print(encode_iso8859_1)

# 'cp437' 无法编码 'ã' (带波形符的 “ã”)。默认的错误处理方式 'strict' 抛出 UnicodeEncodeError。
# encode_cp437 = city.encode('cp437')
# print(encode_cp437)

# error='ignore'处理方式悄无声息地跳过无法编码的字符；这样做通常很是不妥。
encode_cp437 = city.encode('cp437', errors='ignore')
print(encode_cp437)

# 编码时指定 error='replace'，把无法编码的字符替换成 '?'；数据损坏了，但是用户知道出了问题。
encode_cp437 = city.encode('cp437', errors='replace')
print(encode_cp437)

# 'xmlcharrefreplace' 把无法编码的字符替换成 XML 实体。
encode_cp437 = city.encode('cp437', errors='xmlcharrefreplace')
print(encode_cp437)
