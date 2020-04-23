from fp_08_tombola import Tombola


class Fake(Tombola):  # 把 Fake 声明为 Tombola 的子类。

    def pick(self):
        return 13


print(Fake)  # 创建了 Fake 类，目前没有错误。
# <class '__main__.Fake'>

# 尝试实例化 Fake 时抛出了 TypeError。错误消息十分明确：Python 认为 Fake 是抽象类，
# 因为它没有实现 load 方法，这是 Tombola 抽象基类声明的抽象方法之一。
f = Fake()
# Traceback (most recent call last):
#   File "<stdin>", line 14, in <module>
#     f = Fake()
# TypeError: Can't instantiate abstract class Fake with abstract methods load
