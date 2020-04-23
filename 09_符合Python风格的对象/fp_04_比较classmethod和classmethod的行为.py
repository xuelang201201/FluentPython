class Demo:
    @classmethod
    def klassmeth(*args):
        return args  # klassmeth 返回全部位置参数。

    @staticmethod
    def statmeth(*args):
        return args  # statmeth 也是。


print(Demo.klassmeth())  # 不管怎样调用 Demo.klassmeth，它的第一个参数始终是 Demo 类。
print(Demo.klassmeth('spam'))
print(Demo.statmeth())  # Demo.statmeth 的行为与普通的函数相似。
print(Demo.statmeth('spam'))
