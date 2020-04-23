from fp_01_sentence import Sentence

s1 = 'ABC'
for char in s1:
    print(char)

# 如果没有 for 语句，不得不使用 while 循环模拟，要像下面这样写：

s2 = 'ABC'
it = iter(s2)  # 使用可迭代的对象构建迭代器 it。
while True:
    try:
        print(next(it))  # 不断在迭代器上调用 next 函数，获取下一个字符。
    except StopIteration:  # 如果没有字符了，迭代器会抛出 StopIteration 异常。
        del it  # 释放对 it 的引用，即废弃迭代器对象。
        break  # 退出循环。

s3 = Sentence('Pig and Pepper')  # 创建一个 Sentence 实例 s3，包含 3 个单词。
it = iter(s3)  # 从 s3 中获取迭代器。
print(it)
# <iterator object at 0x7faed74dcc40>
print(next(it))
# Pig
print(next(it))
# and
print(next(it))
# Pepper
# print(next(it))  # 没有单词了，因此迭代器抛出 StopIteration 异常。
# Traceback (most recent call last):
#   ...
# StopIteration
print(list(it))  # 到头后，迭代器没用了。
# []
print(list(iter(s3)))  # 如果想再次迭代，要重新构建迭代器。
# ['Pig', 'and', 'Pepper']
