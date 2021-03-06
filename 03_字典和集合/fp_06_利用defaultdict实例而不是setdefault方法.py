"""创建一个从单词到其出现情况的映射"""

import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)  # 把 list 构造方法作为 default_factory 来创建一个 defaultdict。
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)

            # 如果 index 并没有 word 的记录，那么 default_factory 会被调用，
            # 为查询不到的键创建一个值。这个值在这里是一个空的列表，然后这个空
            # 列表被赋值给 index[word]，继而被当作返回值返回，因此 .append(location) 操作总能成功。
            index[word].append(location)


# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])
