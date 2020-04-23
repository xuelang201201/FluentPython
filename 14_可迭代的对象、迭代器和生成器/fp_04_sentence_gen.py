import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:  # 迭代 self.words。
            yield word  # 产出当前的 word。
        # 这个 return 语句不是必要的；这个函数可以直接 “落空”，自动返回。不管有没有 return 语句，
        # 生成器函数都不会抛出 StopIteration 异常，而是在生成完全部值之后会直接退出。
        return

# 完成！  # 不用再单独定义一个迭代器类！
