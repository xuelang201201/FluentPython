import html
from fp_13_singledispatch import htmlize


print(htmlize({1, 2, 3}))  # 默认情况下，在 <pre></pre> 中显示 HTML 转义后的对象字符串表示形式。
print(htmlize(abs))
# 为 str 对象显示的也是 HTML 转义后的字符串表示形式，不过放在 <p></p> 中，而且使用 <br> 表示换行。
print(htmlize('Heimlich & Co.\n- a game'))
print(htmlize(42))  # int 显示为十进制和十六进制两种形式，放在 <pre></pre> 中。
print(htmlize(['alpha', 66, {3, 2, 1}]))  # 各个列表项目根据各自的类型格式化，整个列表则渲染成 HTML 列表。
