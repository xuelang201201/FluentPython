from unicodedata import normalize, name

s1 = 'café'  # 把"e"和重音符组合在一起
s2 = 'cafe\u0301'  # 分解成"e"和重音符
print((s1, s2))
print((len(s1), len(s2)))
print(s1 == s2)

# NFC使用最少的码位构成等价的字符串，而NFD把组合字符分解成基字符和单独的组合字符。
print((len(normalize('NFC', s1)), len(normalize('NFC', s2))))
print((len(normalize('NFD', s1)), len(normalize('NFD', s2))))
print(normalize('NFC', s1) == normalize('NFC', s2))
print(normalize('NFD', s1) == normalize('NFD', s2))

ohm = '\u2126'
print(name(ohm))
ohm_c = normalize('NFC', ohm)
print(name(ohm_c))
print(ohm == ohm_c)
print(normalize('NFC', ohm) == normalize('NFC', ohm_c))

# NFKC 和 NFKD，字母 K 表示 “compatibility”(兼容性)。
# 在 NFKC 和 NFKD 形式中，各个兼容字符会被替换成一个或多个“兼容分解”字符，
# 即便这样有些有些格式损失，但仍是“首选”表述————理想情况下，格式化是外部标记的职责，
# 不应该由 Unicode 处理。
half = '½'
print(normalize('NFKC', half))
four_squared = '4²'
print(normalize('NFKC', four_squared))
micro = '\u00B5'
micro_kc = normalize('NFKC', micro)
print((micro, micro_kc))
print((ord(micro), ord(micro_kc)))
print((name(micro), name(micro_kc)))
