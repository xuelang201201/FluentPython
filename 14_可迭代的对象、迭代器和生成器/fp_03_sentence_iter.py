"""
使用迭代器模式实现 Sentence 类
"""

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    # 与前一版相比，这里只多了一个 __iter__ 方法。这一版没有 __getitem__ 方法，
    # 为的是明确表明这个类可以迭代，因为实现了 __iter__ 方法。
    def __iter__(self):
        return SentenceIterator(self.words)  # 根据可迭代协议，__iter__ 方法实例化并返回一个迭代器。


class SentenceIterator:

    def __init__(self, words):
        self.words = words  # SentenceIterator 实例引用单词列表。
        self.index = 0  # self.index 用于确定下一个要获取的单词。

    def __next__(self):
        try:
            word = self.words[self.index]  # 获取 self.index 索引位上的单词。
        except IndexError:
            raise StopIteration()  # 如果 self.index 索引位上没有单词，那么抛出 StopIteration 异常。
        self.index += 1  # 递增 self.index 的值。
        return word  # 返回单词。

    def __iter__(self):  # 实现 self.__iter__ 方法。
        return self


def main():
    import sys
    import warnings
    try:
        filename = sys.argv[1]
        word_number = int(sys.argv[2])
    except (IndexError, ValueError):
        print('Usage: %s <file-name> <word-number>' % sys.argv[0])
        sys.exit(1)
    with open(filename, 'rt', encoding='utf-8') as text_file:
        s = Sentence(text_file.read())
    for n, word in enumerate(s, 1):
        if n == word_number:
            print(word)
            break
        else:
            warnings.warn('last word is #%d, "%s"' % (n, word))


if __name__ == '__main__':
    main()
