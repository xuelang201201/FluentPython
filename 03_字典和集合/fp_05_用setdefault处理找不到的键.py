"""创建一个从单词到其出现情况的映射"""

import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # 这其实是一种很不好的实现，这样写只是为了证明论点
            # occurrences = index.get(word, [])  # 提取 word 出现的情况，如果还没有它的记录，返回[]。
            # occurrences.append(location)  # 把单词新出现的位置添加到列表的后面。
            # index[word] = occurrences  # 把新的列表放回字典中，这又牵挂到一次查询操作。

            # 获取单词的出现情况列表，如果单词不存在，把单词和一个空列表放进映射，然后返回
            # 这个空列表，这样就能在不进行第二次查找的情况下更新列表了。
            index.setdefault(word, []).append(location)

# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):  # sorted 函数的 key= 参数没有调用 str.upper，而是把这个方法的引
    print(word, index[word])               # 用传递给 sorted 函数，这样在排序的时候，单词会被规范成统一格式。
