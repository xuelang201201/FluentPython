with open('fp_01_mirror.py') as fp:  # <1>fp 绑定到打开的文件上，因为文件的 __enter__ 方法返回 self。
    src = fp.read(60)  # <2>从 fp 中读取一些数据。

print(len(src))
# 60
print(fp)  # <3>fp 变量仍然可用。
# <_io.TextIOWrapper name='fp_01_mirror.py' mode='r' encoding='UTF-8'>
print(fp.closed, fp.encoding)  # <4>可以读取 fp 对象的属性。
# True UTF-8
fp.read(60)  # <5>但是不能在 fp 上执行 I/O 操作，因为在 with 块的末尾，调用 TextIOWrapper.__exit__ 方法把文件关闭了。
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: I/O operation on closed file.
