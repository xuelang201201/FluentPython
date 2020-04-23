"""
把句子划分为单词序列

    >>> s = Sentence('"The time has come," the Walrus said,')  # <1>传入一个字符串，创建一个 Sentence 实例。
    >>> s  # <2>注意，__repr__方法的输出中包含 reprlib.repr 方法生成的 ...。
    Sentence('"The time ha... Walrus said,')
    >>> for word in s:  # <3>Sentence 实例可以迭代。
    ...     print(word)
    The
    time
    has
    come
    the
    Walrus
    said
    >>> list(s)  # <4>因为可以迭代，所以 Sentence 对象可以用于构建列表和其他可迭代的类型。
    ['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']
    >>> s[0]
    'The'
    >>> s[5]
    'Walrus'
    >>> s[-1]
    'said'
"""

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        # <1>re.findall 函数返回一个字符串列表，里面的元素是正则表达式的全部非重叠匹配。
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        # <2>self.words 中保存的是 .findall 函数返回的结果，因此直接返回指定索引位上的单词。
        return self.words[index]

    def __len__(self):  # <3>为了完善序列协议，实现了 __len__ 方法；不过，为了让对象可以迭代，没必要实现这个方法。
        return len(self.words)

    def __repr__(self):
        # <4>reprlib.repr 这个实用函数用于生成大型数据结构的简略字符串表示形式。
        return 'Sentence(%s)' % reprlib.repr(self.text)
