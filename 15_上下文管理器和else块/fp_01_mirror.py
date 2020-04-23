# LookingGlass 上下文管理器类的代码


class LookingGlass:

    def __enter__(self):  # <1>除了 self 之外，Python 调用 __enter__ 方法时不传入其他参数。
        import sys
        # <2>把原来的 sys.stdout.write 方法保存在一个实例属性中，供后面使用。
        self.original_write = sys.stdout.write
        # <3>为 sys.stdout.write 打猴子补丁，替换成自己编写的方法。
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'  # <4>返回 'JABBERWOCKY' 字符串，这样才有内容存入目标变量 what。

    def reverse_write(self, text):  # <5>这是用于取代 sys.stdout.write 的方法，把 text 参数的内容反转，然后调用原来的实现。
        self.original_write(text[::-1])

    # <6>如果一切正常，Python 调用 __exit__ 方法时传入的参数是 None，None，None；
    # 如果抛出了异常，这三个参数是异常数据，如下所述。
    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys  # <7>重复导入模块不会消耗很多资源，因为 Python 会缓存导入的模块。
        sys.stdout.write = self.original_write  # <8>还原成原来的 sys.stdout.write 方法。
        if exc_type is ZeroDivisionError:  # <9>如果有异常，而且是 ZeroDivisionError 类型，打印一个消息……
            print('Please DO NOT divide by zero!')
            return True  # <10>……然后返回 True，告诉解释器，异常已经处理了。
#       <11>如果 __exit__ 方法返回 None，或者 True 之外的值，with 块中的任何异常都会向上冒泡。
