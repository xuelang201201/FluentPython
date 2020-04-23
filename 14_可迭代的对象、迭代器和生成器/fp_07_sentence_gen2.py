"""
在生成器函数中调用 re.finditer 生成器函数，实现 Sentence 类
"""

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text  # <1>不再需要 words 列表。

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # <2>finditer 函数构建一个迭代器，包含 self.text 中匹配 RE_WORD 的单词，产出 MatchObject 实例。
        for match in RE_WORD.finditer(self.text):
            yield match.group()  # <3>match.group() 方法从 MatchObject 实例中提取匹配正则表达式的具体文本。
