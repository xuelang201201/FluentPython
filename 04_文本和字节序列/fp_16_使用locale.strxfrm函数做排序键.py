# 在 Python 中，非 ASCII 文本的标准排序方式是使用 locale.strxfrm函数，根据 locale 模块的文档
# （https://docs.python.org/3/library/locale.html?highlight=strxfrm#locale.strxfrm），这
# 个函数会 “把字符串转换成适合所在区域进行比较的形式”。

import locale

# 中文
print(locale.setlocale(locale.LC_COLLATE, 'zh_CN.UTF-8'))
fruits = ['苹果', '香蕉', '西瓜', '梨', '葡萄', '甘蔗']
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)

# 葡萄牙语
print(locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8'))
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)
